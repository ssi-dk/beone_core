import sys
from ...common.database import get_connection, DB_NAME, WORKSPACES_COL_NAME
from bson.objectid import ObjectId

def trim(item):
    item["id"] = str(item["_id"])
    item.pop("_id", None)
    item.pop("username", None)
    return item

def get_workspaces(user: str):
    conn = get_connection()
    db = conn[DB_NAME]
    workspaces = db[WORKSPACES_COL_NAME]
    return list(map(trim, workspaces.find({"created_by": user})))


def delete_workspace(user: str, workspace_id: str):
    conn = get_connection()
    mydb = conn[DB_NAME]
    workspaces = mydb[WORKSPACES_COL_NAME]

    return workspaces.delete_one(
        {"_id": ObjectId(workspace_id), "created_by": user}
    )