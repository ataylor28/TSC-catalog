import tableauserverclient as TSC
import os
import requests
from authorize import authorize

tableau_auth = authorize.tableau_auth
server = authorize.server

def yes_or_no(question):
    while "Invalid answer! Please respond with y/n":
        reply = str(input(question+' (y/n): ')).lower().strip()
        if reply[:1] =='y':
            return True
        if reply[:1] == 'n':
            return False
        else:
            print("Invalid answer! Please response with y/n")

# create inner func class
class edit_func:

    def group_Flow(self, user_name, group_add):
        cont = yes_or_no("Are you ready to add \"" + str(user_name) + "\" to "+str(group_add)+"? ")
        if cont == True:
            with server.auth.sign_in(tableau_auth):
                all_groups, pagination_item = server.groups.get()
                all_users, pagination_item = server.users.get()
                users = [[user.id, user.name] for user in all_users]
                groups = [[group, group.name] for group in all_groups]
                email_id = [x for x in users[:] if user_name in x]
                email_name = email_id[0][1]
                email_id = email_id[0][0]
                for i in group_add:
                    z = [x for x in groups[:] if i in x]
                    group_item = z[0][0]
                    server.groups.add_user(group_item, email_id)
                    print(str(email_name) + ' was added to ' + str(i))
                print('Finished user provisioning for ' + str(email_name))

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
                        try:
                            server.groups.add_user(x_group, i)
                        except:
                            print("\""+str(i) + "\" is already a member of "+str(x_group))
                        c+=1
                    print(str(c)+' users added to '+ agency)
                else:
                    print(agency +' was already filled.')

    def Users_Need_Groups(self):
        with server.auth.sign_in(tableau_auth):
            all_groups, pagination_item = server.groups.get()
            dict_G = {}
            dict_UG = {}
            groupless = []
            for group in all_groups:
                if group.name == 'LA28 All Staff':
                    dict_G[group.name] = [0]
                    pagination_item = server.groups.populate_users(group)
                    dict_UG[group.name]= [user.name for user in group.users]
                elif group.name == 'Team USA All Staff':
                    dict_G[group.name] = [1]
                    pagination_item = server.groups.populate_users(group)
                    dict_UG[group.name]= [user.name for user in group.users]
            grouped = dict_UG['LA28 All Staff'] + dict_UG['Team USA All Staff']
            all_users, pagination_item = server.users.get()
            list = [user.name for user in all_users if 'admin' not in user.name]
            for user in list:
                if user not in grouped:
                    groupless.append(user)
            print("\nThere are {} users that need to be assigned to a group: ".format(len(groupless)))
            print(*groupless, sep = '\n')
            return groupless
                        
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
            org_Users = [value for key, value in dict_UG.items() if ('LA28 Insights' in key)]
            org_TUSA = [value for key, value in dict_UG.items() if ('Team USA All Staff' in key)]
            org_Market = [value for key, value in dict_UG.items() if ('LA28 Marketing' in key)]
            org_Add_TUSA = []
            org_Add_Market = []
            # Add insights to LA28 Marketing
            for i in org_Users[0]:
                if i not in org_Market[0]:
                    org_Add_Market.append(i)
            if org_Add_Market:
                c=0
                for i in org_Add_Market:
                    x = dict_G['LA28 Marketing'][0]
                    x_group = all_groups[x]
                    try:
                        server.groups.add_user(x_group, i)
                    except:
                        print("\""+str(i) + "\" is already a member of "+str(x_group))
                    c+=1
                print(str(c)+' insights users added to LA28 Marketing')
            else:
                print('LA28 Marketing was already filled with insights users.')
            # Add insights to TUSA All Staff
            for i in org_Users[0]:
                if i not in org_TUSA[0]:
                    org_Add_TUSA.append(i)
            if org_Add_TUSA:
                c=0
                for i in org_Add_TUSA:
                    x = dict_G['Team USA All Staff'][0]
                    x_group = all_groups[x]
                    try:
                        server.groups.add_user(x_group, i)
                    except:
                        print("\""+str(i) + "\" is already a member of "+str(x_group))
                    c+=1
                print(str(c)+' insights users added to Team USA All Staff')
            else:
                print('Team USA All Staff was already filled with insights users.')

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
                        try:
                            server.groups.add_user(x_group, i)
                        except:
                            print("\""+str(i) + "\" is already a member of "+str(x_group))
                        c+=1
                    print(str(c)+' users added to '+ org_str)
                else:
                    print(org_str +' was already filled.')