# flowchart
from audioop import add
from read import read_func

read = read_func()

#u_email = str(input("What is the new user's email? "))

from requests import NullHandler


def yes_or_no(question):
    while "Invalid answer! Please response with y/n":
        reply = str(input(question+' (y/n): ')).lower().strip()
        if reply[:1] =='y':
            return True
        if reply[:1] == 'n':
            return False
        else:
            print("Invalid answer! Please response with y/n")



def flow_AMP():
    q1 = yes_or_no("Is this an AMP User?")
    if q1 == True:
        while "Invalid answer! Please response with y/n":
            q = yes_or_no("Is this an AMP Editor?")
            if q == True:
                status_AMP = 'AMP Editors'
                return status_AMP
            if q == False:
                status_AMP = 'AMP'
                return status_AMP
            else:
                print("Invalid answer! Please response with y/n")

def flow_domain():
    while "Invalid answer! Please response with 1, 2 or 3":
        reply = int(input("Where does this user work? "+'\n'+'1. LA28'+'\n'+'2. USOPC'+'\n'+'3. Agency'+'\n'))
        if reply == 1:
            status_domain = 'LA28'
            return status_domain
        if reply == 2:
            status_domain ='USOPC'
            return status_domain
        if reply == 3:
            status_domain = 'Agency'
            return status_domain
        else:
            print("Invalid answer! Please response with 1, 2 or 3")

groups_available = read.groups()
add_to_groups = []

def department_LA28():
    #filt = [x for x in groups_available if 'Leadership' in x or 'Agency'in x or 'Staff' in x or 'Insights' in x]
    #print(filt)
    groups_la28 = [x for x in groups_available if 'LA28' in x]
    groups_la28[:] = (x for x in groups_la28 if 'Leadership' not in x and 'Agency' not in x and 'Staff' not in x and 'Insights' not in x)
    while "False":
        reply = 0
        i = 1
        for g in groups_la28:
            print (str(i)+'. '+ g)
            i+=1
        reply = int(input("Which department is the user in? "))
        choice = groups_la28[reply-1]
        reply1 = yes_or_no("You chose \""+str(choice)+"\" is that correct?")
        if reply1 == True: break
        if reply1 == False: continue
    if choice == 'LA28 Marketing':
        q1 = yes_or_no("Is this user on the Insights Team?")
        if q1 == True:
            choice = 'LA28 Insights'
        else: choice = 'LA28 Marketing'
    else: choice
    return choice

add_to_groups= []

def flow_LA28():
    q1 = yes_or_no("Is this an user a part of Leadership?")
    if q1 == True:
        add_to_groups.append('LA28 Leadership')
        q2 = yes_or_no("Want to add a department?")
        if q2 == True:
            add_to_groups.append(department_LA28())
        return add_to_groups
    if q1 == False:
        add_to_groups.append(department_LA28())
        return add_to_groups
    #if q1 == False:

print(flow_LA28())

    





