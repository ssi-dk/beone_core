from flask import abort
from flask.json import jsonify
from ..repositories.workspaces import get_workspaces as get_workspaces_db
from ..repositories.workspaces import delete_workspace as delete_workspace_db
from ..repositories.workspaces import delete_workspace_sample as delete_workspace_sample_db
from ..repositories.workspaces import create_workspace as create_workspace_db
from ..repositories.workspaces import create_workspace_from_sequence_ids as create_workspace_from_sequence_ids_db
from ..repositories.workspaces import clone_workspace as clone_workspace_db
from ..repositories.workspaces import update_workspace as update_workspace_db
from ..repositories.workspaces import get_workspace as get_workspace_db
from ..repositories.workspaces import get_workspace_data as get_workspace_data_db
from ..utils import validate_sample_ids

def get_workspaces(user, token_info):
    return jsonify(get_workspaces_db(user))

def delete_workspace(user, token_info, workspace_id: str):
    res = delete_workspace_db(user, workspace_id)
    return None if res.deleted_count > 0 else abort(404)

def create_workspace(user, token_info, body):
    if body.samples:
        validate_sample_ids(body.samples)

    res = create_workspace_db(user, body)

    if res.upserted_id:
        return jsonify({"id": str(res.upserted_id)})
    return jsonify(body)

def create_workspace_from_sequence_ids(user, token_info, body):
    if body.samples:
        validate_sample_ids(body.samples)

    res = create_workspace_from_sequence_ids_db(user, body)
    
    if res.upserted_id:
        return jsonify({"id": str(res.upserted_id)})
    return jsonify(body)

def clone_workspace(user, token_info, body):
    res = clone_workspace_db(user, body)

    if not res.inserted_id:
        return None
    
    return jsonify({"id": str(res.inserted_id)})

def post_workspace(user, token_info, workspace_id: str, body):
    if body.samples:
        validate_sample_ids(body.samples)

    update_workspace_db(user, workspace_id, body)

    return jsonify(body)

def get_workspace(user, token_info, workspace_id: str):
    return jsonify(get_workspace_db(user, workspace_id))

def delete_workspace_sample(user, token_info, workspace_id, sample_id):
    res = delete_workspace_sample_db(user, workspace_id, sample_id)
    return None if res.modified_count > 0 else abort(404)

def get_workspace_data(user, token_info, workspace_id):
    res = get_workspace_data_db(user, token_info, workspace_id)

    if res is None:
        return abort(404)

    return res
