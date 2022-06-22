# flowchart
from audioop import add
from read import read_func
from flow_def import flow_func

read = read_func()
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

def get_email():
    while "False":
        u_email = str(input("What is the new user's email? "))
        reply1 = yes_or_no("You wrote \""+str(u_email)+"\" is that correct?")
        if reply1 == True: break
        if reply1 == False: continue
    return u_email

def user_provision():
    AMP = flow._AMP()
    if AMP != None:
        if AMP[0] == True:
            z = AMP[1]
            print(AMP[1])
            add_to_groups = flow._domain()
            add_to_groups.append(z)
            return add_to_groups
        elif AMP[0] == False:
            add_to_groups = AMP[1]
            print(add_to_groups)
            return add_to_groups
    elif AMP == None: 
        add_to_groups = flow._domain()
    return add_to_groups

dict = {get_email(): user_provision()}

print(dict)

    





