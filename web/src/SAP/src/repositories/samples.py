from typing import Any, Dict
from ...common.database import (
    get_connection,
    DB_NAME,
    SAMPLES_COL_NAME,
)
from bson.objectid import ObjectId

def get_single_sample(sequence_id: str) -> Dict[str, Any]:
    conn = get_connection()
    mydb = conn[DB_NAME]
    samples = mydb[SAMPLES_COL_NAME]
    return samples.find_one({"categories.sample_info.summary.sofi_sequence_id": f"{sequence_id}"}, {"_id": 0})

def get_single_sample_by_object_id(id: str) -> Dict[str, Any]:
    conn = get_connection()
    mydb = conn[DB_NAME]
    samples = mydb[SAMPLES_COL_NAME]
    return samples.find_one(ObjectId(id))
