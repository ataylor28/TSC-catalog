# flowchart
from audioop import add
from heapq import heapify
from mimetypes import init
from re import T
from turtle import end_fill

from tableauserverclient import ServerResponseError
from read import read_func
from edit import edit_func
from flow_def import flow_func
from authorize import authorize

tableau_auth = authorize.tableau_auth
server = authorize.server

read = read_func()
edit = edit_func()
flow = flow_func()

def yes_or_no(question):
    while "Invalid answer! Please response with y/n":
        reply = str(input(question+' (y/n): ')).lower().strip()
        if reply[:1] =='y':
            return True
        if reply[:1] == 'n':
            return False
        else:
            print("Invalid answer! Please response with y/n")


def user_provision():
    AMP = flow._AMP()
    if AMP != None:
        if AMP[0] == True:
            z = AMP[1]
            add_to_groups2 = flow._domain()
            add_to_groups2.append(z)
            return add_to_groups2
        elif AMP[0] == False:
            add_to_groups2 = AMP[1]
            return [add_to_groups2]
    elif AMP == None: 
        add_to_groups2 = flow._domain()
        return add_to_groups2
    return add_to_groups2

method = int(input("How would you like to provision users? "+'\n'+'1. Individually by email'+'\n'+'2. By list'+'\n'))

# Individually by email
if method == 1:
    e = flow.get_email()
    g = user_provision()
    #for group in g:
    cont = yes_or_no("Are you ready to add \"" + str(e) + "\" to "+str(g)+"? ")
    if cont == True:
        try:
            edit.group_Flow(e, g)
        except ServerResponseError:
            print("\""+str(e) + "\" is already a member of "+str(g))
elif method == 2:
    groupless = []
    groupless = edit.Users_Need_Groups()
    for e in groupless:
        g = []
        print ('\n\nProvisioning for ' + e)
        g = user_provision()
        for i in g:
            try:
                edit.group_Flow(e, g)
                g.clear()
            except ServerResponseError:
                print("\""+str(e) + "\" is already a member of "+str(i))
                g.clear()
            
# Automate flow
edit.group_Agency()
edit.group_AllStaff()
edit.group_Insights()
