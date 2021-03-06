import tableauserverclient as TSC
import os
import requests
from authorize import authorize

tableau_auth = authorize.tableau_auth
server = authorize.server

def group_AllStaff():
    with server.auth.sign_in(tableau_auth):
        all_groups, pagination_item = server.groups.get()
        dict_G = {}
        dict_UG = {}
        g = 0
        for group in all_groups :
            dict_G[group.name] = [g]
            g+=1
            pagination_item = server.groups.populate_users(group)
            dict_UG[group.name]= [user.id for user in group.users]
        for org in ['la28', 'team usa']:
            if org == 'la28':
                org_str = 'LA28 All Staff'
            elif org == 'team usa':
                org_str = 'Team USA All Staff'
            org_Users2 = [value for key, value in dict_UG.items() if (org in key.lower() and org_str not in key)]
            org_Users = []
            for i in org_Users2:
                if i:
                    org_Users.extend(i)
            org_AllStaff2 = [value for key, value in dict_UG.items() if (org_str in key)]
            org_AllStaff = org_AllStaff2[0]
            org_Add = []
            for i in org_Users:
                if i not in org_AllStaff:
                    org_Add.append(i)
                else:
                    continue
            if org_Add:
                c=0
                for i in org_Add:
                    x = dict_G[org_str][0]
                    x_group = all_groups[x]
                    #all_groups, pagination_item = server.groups.get()
                    server.groups.add_user(x_group, i)
                    c+=1
                print(str(c)+' users added to '+ org_str)
            else:
                print(org_str +' was already filled.')

group_AllStaff()