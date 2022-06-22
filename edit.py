import tableauserverclient as TSC
import os
import requests
from authorize import authorize

tableau_auth = authorize.tableau_auth
server = authorize.server

# create inner func class
class edit_func:

    def group_Flow(self, user_name, group_add):
        with server.auth.sign_in(tableau_auth):
            all_groups, pagination_item = server.groups.get()
            all_users, pagination_item = server.users.get()
            users = [[user.id, user.name] for user in all_users]
            print(users)
            groups = [[group, group.name] for group in all_groups]
            email_id = [x for x in users[:] if user_name in x]
            email_name = email_id[0][1]
            email_id = email_id[0][0]
            for i in group_add:
                print(i)
                z = [x for x in groups[:] if i in x]
                group_item = z[0][0]
                server.groups.add_user(group_item, email_id)
                print(str(email_name) + ' was added to ' + str(i))
            print('Finished user provisioning for ' + str(email_name))


    def group_AllStaff(self):
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
                    org_Users = [value for key, value in dict_UG.items() if (org in key.lower() and org_str not in key and 'agency' not in key.lower())]
                    org_AllStaff = [value for key, value in dict_UG.items() if (org_str in key and 'agency' not in key.lower())]
                    org_Add = []
                    for i in org_Users:
                        if i not in org_AllStaff:
                            org_Add+=i
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

    # Both Agency to LA28 Agency & Team USA Agency
    def group_Agency(self):
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
            for agency in ['LA28 Agency', 'Team USA Agency']:
                both = [value for key, value in dict_UG.items() if ('both agency'in key.lower())]
                org_Agency = [value for key, value in dict_UG.items() if (agency in key)]
                org_Add = []
                for i in both:
                    if i not in org_Agency:
                        org_Add+=i
                    else:
                        continue
                if org_Add:
                    c=0
                    for i in org_Add:
                        x = dict_G[agency][0]
                        x_group = all_groups[x]
                        #all_groups, pagination_item = server.groups.get()
                        server.groups.add_user(x_group, i)
                        c+=1
                    print(str(c)+' users added to '+ agency)
                else:
                    print(agency +' was already filled.')

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
                    org_Users = [value for key, value in dict_UG.items() if (org in key.lower() and org_str not in key and 'agency' not in key.lower())]
                    org_AllStaff = [value for key, value in dict_UG.items() if (org_str in key and 'agency' not in key.lower())]
                    org_Add = []
                    for i in org_Users:
                        if i not in org_AllStaff:
                            org_Add+=i
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
                        
    def group_Insights(self):
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
            for insights in ['LA28 Marketing', 'Team USA All Staff']:
                insight = [value for key, value in dict_UG.items() if ('insights'in key.lower())]
                org_Insight = [value for key, value in dict_UG.items() if (insights in key)]
                org_Add = []
                for i in insights:
                    if i not in org_Insight:
                        org_Add+=i
                    else:
                        continue
                if org_Add:
                    c=0
                    for i in org_Add:
                        x = dict_G[insights][0]
                        x_group = all_groups[x]
                        #all_groups, pagination_item = server.groups.get()
                        server.groups.add_user(x_group, i)
                        c+=1
                    print(str(c)+' users added to '+ insight)
                else:
                    print(insight +' was already filled.')
        