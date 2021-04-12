import os, sys
import binascii
from typing import Dict

from pymongo import MongoClient, mongo_client
from pymongo.encryption import Algorithm, ClientEncryption
from pymongo.encryption_options import AutoEncryptionOpts

DEBUG = os.getenv("DEBUG", "False").lower() in ["true", "1"]

CONNECTION = None
CLIENT_ENC = None

BIFROST_MONGO_CONN = os.environ.get(
    "BIFROST_MONGO_CONN", "mongodb://localhost:27017/bifrost_test"
)
DB_NAME = os.environ.get("BIFROST_MONGO_DB", "bifrost_test")
ANALYSIS_COL_NAME = "sap_analysis_results"
APPROVALS_COL_NAME = "sap_approvals"
USERVIEWS_COL_NAME = "user_views"
QUEUE_COL_NAME = "sap_broker_queue"
MANUAL_METADATA_COL_NAME = "sap_manual_metadata"
TBR_METADATA_COL_NAME = "sap_tbr_metadata"
LIMS_METADATA_COL_NAME = "sap_lims_metadata"

SOFI_BIFROST_ENCRYPTION_NAMESPACE = os.environ.get(
    "SOFI_BIFROST_ENCRYPTION_NAME", "encryption.sap_pii"
)
(
    ENCRYPTION_DB,
    ENCRYPTION_KEY_NAME,
) = SOFI_BIFROST_ENCRYPTION_NAMESPACE.split(".", 1)

isolate_column = "display_name"
institution_column = "categories.sample_info.summary.institution"

# The MongoClient is thread safe and pooled, so no problem sharing it :)
def get_connection(with_enc=False):
    """
    Returns instance of global pooled connection.
    The connection instance has automatic decryption enabled.
    -> MongoClient
    If with_enc=True this returns a ClientEncryption used for encryption fields along the connection
    -> MonogClient, ClientEncryption
    """
    global CONNECTION
    global CLIENT_ENC
    if CONNECTION is not None and CLIENT_ENC is not None:
        if with_enc:
            return CONNECTION, CLIENT_ENC
        else:
            return CONNECTION

    else:
        # Key must be 96 bytes
        local_master_key_raw = os.environ["SOFI_BIFROST_ENCRYPTION_KEY"]
        local_master_key = binascii.a2b_base64(local_master_key_raw.encode())

        kms_providers = {"local": {"key": local_master_key}}
        # The MongoDB namespace (db.collection) used to store
        # the encryption data keys.
        key_vault_namespace = SOFI_BIFROST_ENCRYPTION_NAMESPACE
        key_vault_db_name, key_name = (
            ENCRYPTION_DB,
            ENCRYPTION_KEY_NAME,
        )

        # bypass_auto_encryption=True disable automatic encryption but keeps
        # the automatic _decryption_ behavior. bypass_auto_encryption will
        # also disable spawning mongocryptd.
        auto_encryption_opts = AutoEncryptionOpts(
            kms_providers, key_vault_namespace, bypass_auto_encryption=True
        )

        client = (
            MongoClient(auto_encryption_opts=auto_encryption_opts)
            if DEBUG
            else MongoClient(
                BIFROST_MONGO_CONN, auto_encryption_opts=auto_encryption_opts
            )
        )
        coll = client.test.coll

        # First time key setup. Index creation in mongo is idempotent
        key_vault = client[key_vault_db_name][key_name]
        key_vault.create_index(
            "keyAltNames",
            unique=True,
            partialFilterExpression={"keyAltNames": {"$exists": True}},
        )

        client_encryption = ClientEncryption(
            kms_providers,
            key_vault_namespace,
            # The MongoClient to use for reading/writing to the key vault.
            # This can be the same MongoClient used by the main application.
            client,
            # The CodecOptions class used for encrypting and decrypting.
            # This should be the same CodecOptions instance you have configured
            # on MongoClient, Database, or Collection.
            coll.codec_options,
        )

        existing = client[key_vault_db_name][key_name].find_one()
        if existing is None:
            client_encryption.create_data_key("local", key_alt_names=[key_name])

        CONNECTION = client
        CLIENT_ENC = client_encryption
        if with_enc:
            return CONNECTION, CLIENT_ENC
        else:
            return CONNECTION


def encrypt_dict(encryption_client: ClientEncryption, dikt: Dict, filter_list=None):
    """
    Encrypt fields of a dict, possible filtered by a an array as kwarg "filter"
    """
    if filter_list is not None:
        for filter_item in filter_list:
            if filter_item in dikt:
                encrypted_field = encryption_client.encrypt(
                    dikt[filter_item],
                    Algorithm.AEAD_AES_256_CBC_HMAC_SHA_512_Deterministic,
                    key_alt_name=ENCRYPTION_KEY_NAME,
                )
                dikt[filter_item] = encrypted_field
    else:
        for key, value in dikt.items():
            encrypted_field = encryption_client.encrypt(
                value,
                Algorithm.AEAD_AES_256_CBC_HMAC_SHA_512_Deterministic,
                key_alt_name=ENCRYPTION_KEY_NAME,
            )
            dikt[key] = encrypted_field


def yield_chunks(cursor, chunk_size=200):
    """
    Generator to yield chunks from cursor
    :param cursor:
    :param chunk_size:
    """
    chunk = []
    for i, row in enumerate(cursor):
        if i % chunk_size == 0 and i > 0:
            yield chunk
            del chunk[:]
        chunk.append(row)
    yield chunk
