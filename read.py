import tableauserverclient as TSC
import os
import requests
import pandas as pd
from authorize import authorize
from hierarchy import main

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
            lst = []
            list1 = [group.name for group in all_groups]
            return list1
            for group in all_groups :
                lst = lst.append(group.name)
                print(group.name)
    
    # create read_users function:
    def users(self):
        with server.auth.sign_in(tableau_auth):
            all_users, pagination_item = server.users.get()
            print("\nThere are {} users on site: ".format(pagination_item.total_available))
            list2 = [user.id for user in all_users]
            list = [user.name for user in all_users]
            print(*list2, sep = '\n')
    
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
        
        class hier:
            
            def getProjects():
                # Get all projects
                all_projects = list(TSC.Pager(server.projects))
                project_list = []
                for project in all_projects:
                    project_list.append((project.name, project.id, project.parent_id))
                # Create dataframe of relevant attributes
                project_df = pd.DataFrame(data=project_list, columns=['ProjectNM', 'ProjectID', 'ParentProjectID'])
                # Map project to parent project
                project_to_parent = {project.id: project.parent_id for project in all_projects}
                # Map project to name
                project_to_name = {project.id: project.name for project in all_projects}
                return project_df, project_to_parent, project_to_name

            def getHierarchy(project_id, parent_list=None):
                if parent_list == None:
                    parent_list = []
                parent_list.append(project_id)
                # reset project id to parent project id
                project_id = project_to_parent[project_id]
                # if there's a parent id, loop through again
                if project_id:
                    getHierarchy(project_id, parent_list)
                return parent_list

            def getProjectHierarchy(project_df):
                project_df['PathDSC'] = project_df.ProjectID.apply(getHierarchy)
                project_df['PathLevelNBR'] = project_df.apply(lambda row: len(row.PathDSC), axis=1)
                project_df.sort_values(by='PathLevelNBR', ignore_index=True, inplace=True)
                return project_df

            if __name__ == '__main__':
                # Grab credentials from env file
                tableau_auth = authorize.tableau_auth
                server = authorize.server
                # Sign into server
                with server.auth.sign_in(tableau_auth):
                    server.use_server_version()
                    project_df, project_to_parent, project_to_name = getProjects()
                    hierarchy_df = getProjectHierarchy(project_df)
                    # Get current path of script
                    filepath = Path(Path(__file__).parent) / 'zzzOutputs'
                    filepath.mkdir(exist_ok=True)
                    filename = filepath / 'ProjectHierarchy.csv'
                    hierarchy_df.to_csv(filename, index=False)




