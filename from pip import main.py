from pip import main
import tableauserverclient as TSC
import pandas as pd
from pathlib import Path
import os
from authorize import authorize

tableau_auth = authorize.tableau_auth
server = authorize.server
with server.auth.sign_in(tableau_auth):
    
    all_projects, pagination_item = server.projects.get()

    for project in all_projects:
        print(project.parent_id)
        if project.id:
            parent_project_id = project.id

    project_ids = list()
    for project in all_projects:
        if project.parent_id == parent_project_id:
            project_ids.append(project.id)

    print(project_ids)
