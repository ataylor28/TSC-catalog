import tableauserverclient as TSC
import os
import requests
import pandas as pd
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
    
    # create read users_by_group function
    def users_by_group(self):
            with server.auth.sign_in(tableau_auth):
                all_groups, pagination_item = server.groups.get()
                dict_G = {}
                dict_UG = {}
                g = 0
                for group in all_groups :
                    dict_G[group.name] = [g]
                    g+=1
                    pagination_item = server.groups.populate_users(group)
                    dict_UG[group.name]= [user.name for user in group.users]
                print("\n".join("{}\n{}\n".format(k, v) for k, v in dict_UG.items()))
    
    # create read_users function:
    def users_and_permissions(self):
        with server.auth.sign_in(tableau_auth):
            all_users, pagination_item = server.users.get()
            list_UP = [[user.name, user.site_role] for user in all_users]
            print("\n".join("{}, {}".format(k, v) for k, v in list_UP[:]))
            
            
    
    # create read workbooks by project function
    def workbooks_by_project(self):
            with server.auth.sign_in(tableau_auth):
                all_projects, pagination_item = server.projects.get()
                pagination_item = server.projects.populate_permissions(all_projects)
                list = [project for project in all_projects]
                print(*list, sep = '\n')
# create read_projects function
    def project_permissions(self):
        with server.auth.sign_in(tableau_auth):
            all_projects, pagination_item = server.projects.get()
            dict_G = {}
            dict_UG = {}
            g = 0
            for project in all_projects :
                dict_G[project.name] = [g]
                g+=1
                print(project.name)
                pagination_item = server.projects.populate_permissions(project)
                #dict_UG[project.name]= [permission for permission in project.permissions]
                permissions = project.permissions
                i = -1
                for rule in permissions:
                    i +=1
                    group_user_type = permissions[i].grantee.tag_name
                    group_user_id = permissions[i].grantee.id
                    group_user_capabilities = permissions[i].capabilities
                    if group_user_type == 'user':
                        user_item = server.users.get_by_id(permissions[i].grantee.id)
                        group_user_name = user_item.name
                    elif group_user_type == 'group':
                        for group_item in TSC.Pager(server.groups):
                            if group_item.id == group_user_id:
                                group_user_name = group_item.name
                                break
                    print('Type: %s\tName: %s\tCapabilities: %s' %(group_user_type, group_user_name, group_user_capabilities))



