# flowchart
from audioop import add
from read import read_func

read = read_func()

#u_email = str(input("What is the new user's email? "))
groups_available = read.groups()
add_to_groups = []

from requests import NullHandler

def yes_or_no(question):
    while "Invalid answer! Please respond with y/n":
        reply = str(input(question+' (y/n): ')).lower().strip()
        if reply[:1] =='y':
            return True
        if reply[:1] == 'n':
            return False
        else:
            print("Invalid answer! Please response with y/n")

class flow_func():

    def get_email(self):
        while "False":
            u_email = str(input("What is the new user's email? "))
            reply1 = yes_or_no("You wrote \""+str(u_email)+"\" is that correct?")
            if reply1 == True: break
            if reply1 == False: continue
        return u_email


    def _AMP(self):
        q1 = yes_or_no("Is this an AMP User?")
        if q1 == True:
            while "Invalid answer! Please response with y/n":
                q = yes_or_no("Is this an AMP Editor?")
                if q == True:
                    status_AMP = 'AMP Editors'
                    z = yes_or_no('Continue?')
                    return [z, status_AMP]
                if q == False:
                    status_AMP = 'AMP'
                    z = yes_or_no('Continue?')
                    return [z, status_AMP]
                else:
                    print("Invalid answer! Please response with y/n")

    def _domain(self):
        reply = int(input("Where does this user work? "+'\n'+'1. LA28'+'\n'+'2. USOPC'+'\n'+'3. Agency'+'\n'))
        # LA28
        a = []
        if reply == 1:
            #add_to_groups = None
            status_domain = 'LA28'
            q1 = yes_or_no("Is this an user a part of C-Suite Leadership?")
            if q1 == True:
                #add_to_groups.append('LA28 Leadership')
                q2 = yes_or_no("Want to add a department?")
                if q2 == True:
                    self.LA28_domain._Department()
                    a = self.add_to_groups.append('LA28 Leadership')
                elif q2 == False:
                    a = self.add_to_groups.append('LA28 Leadership')
                return a
            if q1 == False:
                a = self.LA28_domain._Department()
                return a
        # Team USA
        if reply == 2:
            #add_to_groups = None
            status_domain ='USOPC'
            q1 = yes_or_no("Is this an user a part of C-Suite Leadership?")
            if q1 == True:
                q2 = yes_or_no("Want to add a department?")
                if q2 == True:
                    self.TUSA_domain._Department()
                    self.add_to_groups.append('Team USA Leadership')
                if q2 == False:
                    self.add_to_groups.append('Team USA Leadership')
                return add_to_groups
            if q1 == False:
                self.TUSA_domain._Department()
            return add_to_groups
        if reply == 3:
            #add_to_groups = None
            status_domain = 'Agency'
            self.Agency_domain._Department()
            return add_to_groups
        else:
            print("Invalid answer! Please response with 1, 2 or 3")

    class LA28_domain():
        
        def _Department():
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
                elif reply1 == False: continue
            if choice == 'LA28 Marketing':
                q2 = yes_or_no("Is this user part of Marketing Leadership?")
                if q2 == True:
                    q3 = yes_or_no("Is this user on the Insights Team?")
                    if q3 == True:
                        add_to_groups.append('LA28 Insights')
                        add_to_groups.append('LA28 & Team USA Marketing Leadership')
                    else:
                        add_to_groups.append('LA28 Marketing')
                        add_to_groups.append('LA28 & Team USA Marketing Leadership')
                elif q2 == False: 
                    q3 = yes_or_no("Is this user on the Insights Team?")
                    if q3 == True:
                        add_to_groups.append('LA28 Insights')
                    else: add_to_groups.append('LA28 Marketing')
                    #add_to_groups.append(choice)
            elif choice == 'LA28 Commercial':
                q1 = yes_or_no("Is this user part of Commercial Leadership?")
                if q1 == True:
                    add_to_groups.append('LA28 Commercial')
                    add_to_groups.append('LA28 Commercial Leadership')
                else: add_to_groups.append('LA28 Commercial')
            else: add_to_groups.append(choice)
            return add_to_groups
        
    class TUSA_domain():

        def _Department():
            groups_TUSA = [x for x in groups_available if 'Team USA' in x]
            groups_TUSA[:] = (x for x in groups_TUSA if 'Leadership' not in x and 'Agency' not in x and 'Staff' not in x)
            while "False":
                reply = 0
                i = 1
                for g in groups_TUSA:
                    print (str(i)+'. '+ g)
                    i+=1
                reply = int(input("Which department is the user in? "))
                choice = groups_TUSA[reply-1]
                reply1 = yes_or_no("You chose \""+str(choice)+"\" is that correct?")
                if reply1 == True: break
                if reply1 == False: continue
            if choice == 'Team USA Digital':
                q1 = yes_or_no("Is this user part of Digital/Marketing Leadership?")
                if q1 == True:
                    add_to_groups.append('Team USA Digital')
                    add_to_groups.append('LA28 & Team USA Marketing Leadership')
                else: add_to_groups.append('Team USA Digital')
            else: add_to_groups.append(choice)
            return add_to_groups

    class Agency_domain():
        
        def _Department():
            groups_Agency = [x for x in groups_available if 'Agency' in x]
            while "False":
                reply = 0
                i = 1
                for g in groups_Agency:
                    print (str(i)+'. '+ g)
                    i+=1
                reply = int(input("Which department is the user in? "))
                choice = groups_Agency[reply-1]
                reply1 = yes_or_no("You chose \""+str(choice)+"\" is that correct?")
                if reply1 == True: break
                if reply1 == False: continue
            add_to_groups.append(choice)
            choice = None
            return add_to_groups