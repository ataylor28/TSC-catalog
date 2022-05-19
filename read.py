import tableauserverclient as TSC
import os
import requests
from authorize import authorize

tableau_auth = authorize.tableau_auth
server = authorize.server

# create inner func class
class read_func:

    # create read_datasource function
    def datasource(self):
        with server.auth.sign_in(tableau_auth):
            all_datasources, pagination_item = server.datasources.get()
            print("\nThere are {} data sources on site: ".format(pagination_item.total_available))
            list = [datasource.name for datasource in all_datasources]
            print(*list, sep ="\n")

    # create read_groups function
    def groups(self):
        with server.auth.sign_in(tableau_auth):
            all_groups, pagination_item = server.groups.get()
            for group in all_groups :
                print(group.name)
    
    # create read_users function:
    def users(self):
        with server.auth.sign_in(tableau_auth):
            all_users, pagination_item = server.users.get()
            print("\nThere are {} users on site: ".format(pagination_item.total_available))
            list = [user.name for user in all_users]
            print(*list, sep = '\n')
    
    #create read_workbooks function
    def workbooks(self):
        with server.auth.sign_in(tableau_auth):
            all_workbooks, pagination_item = server.workbooks.get()
            print("\nThere are {} workbooks on site: ".format(pagination_item.total_available))
            list = [workbook.name for workbook in all_workbooks]
            print(*list, sep = '\n')
    
    # create read_projects function
    def projects(self):
        with server.auth.sign_in(tableau_auth):
            all_projects, pagination_item = server.projects.get()
            print("\nThere are {} projects on site: ".format(pagination_item.total_available))
            list = [project.name for project in all_projects]
            print(*list, sep = '\n')