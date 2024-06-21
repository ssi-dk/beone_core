import sys
import os
from flask import abort
from flask.json import jsonify
from .....microreact_integration.functions import new_project as new_microreact_project
from ..repositories.workspaces import get_workspace as get_workspace_db
from web.src.SAP.src.security.permission_check import (authorized_columns)

def send_to_microreact(user, token_info, body):
    ws_id = body.workspace 
    ws = get_workspace_db(user, ws_id)
     
    authorized = authorized_columns(token_info)
    print(authorized, file=sys.stderr)
    print(ws["samples"], file=sys.stderr)

    values = []
    for sample in ws["samples"] :
        row = []
        for column in authorized :
            if column in sample:
                row.append(sample[column])
            else:
                row.append("")
        values.append(row)

    print(values, file=sys.stderr)
    

    res = new_microreact_project(        
        project_name=ws["name"],
        tree_calcs=[],
        metadata_keys=authorized,
        metadata_values=values,
        mr_access_token=body.mr_access_token,
        mr_base_url="http://microreact:3000/"
        )

    return jsonify(res.json())
