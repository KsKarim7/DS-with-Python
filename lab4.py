# https://docs.google.com/document/d/19f_lVAgsnCHkvk6SrJ4MmZMyGauLnADsyxON711bex0/edit?usp=drive_link

class Patient:
    def __init__(self, id, name, age, bgrp, n, p):
        # count = 0
        # if (count == 0):
        #     self.id = 1
        #     count += 1
        # else:
        #     self.id = id+1
        self.id = id
        self.name = name
        self.age = age
        self.bgrp = bgrp
        self.next = n
        self.prev = p


class WRM:
    def __init__(self):
        self.dp = Patient(None, None, None, None, None, None)
        self.dp.next = self.dp
        self.prev = self.dp
        self.tail = self.dp

    def RegisterPatient(self, id, name, age, bloodgroup):
        node = Patient(id, name, age, bloodgroup, self.dp, self.tail)
        self.tail.next = node
        self.tail = self.tail.next
        self.dp.prev = self.tail

    def servePatient(self):
        if (self.dp.next == self.dp and self.dp.prev == self.dp):
            print("No patient available.")
        else:
            node = self.dp.next
            print(f'{node.name} is served. \n')
            prev = node.prev
            nex = node.next
            prev.next = nex
            nex.prev = prev

    def cancelAll(self):
        self.dp.next = self.dp
        self.dp.prev = self.dp

    def canDocGoHome(self):
        if (self.dp.next == self.dp and self.dp.prev == self.dp):
            return True
        else:
            return False

    def showAllpatient(self):
        temp = self.dp.next
        if (self.dp.next == self.dp and self.dp.prev == self.dp):
            print("No appointments left for today. \n")
        while (temp != self.dp):
            print(
                f'Patient Details: \nID: {temp.id}: Name: {temp.name}  Age: {temp.age} Blood Group: {temp.bgrp} \n')
            temp = temp.next

    def reverseTheLine(self):
        temp = self.dp.next
        tempp = self.tail
        while (temp != tempp):
            n = temp.elem
            temp.elem = tempp.elem
            tempp.elem = n
            temp = temp.next
            tempp = tempp.prev


def main():
    print("**Welcome to Waiting Room Management System**\n==Choose an Option==")

    system = WRM()
    while (True):
        inp = int(input("1. Register Patient. \n2. Serve patient. \n3. Cancel All. \n4. Can Doctor Go Home? \n5. Show All Patient. \n6. Exit. \n==================== \nEnter your choice: "))

        if (inp == 1):
            print("For registration kindly fill up the given form: \n")
            id = input("ID: ")
            name = input("Name: ")
            age = input("Age: ")
            bgrp = input("Blood Group: ")
            system.RegisterPatient(id, name, age, bgrp)
            print("Patient has been registered successfully! \nThank you.")
        elif (inp == 5):
            print("List of all patients is given below: \n")
            system.showAllpatient()
        elif (inp == 2):
            print('Serving the first patient of the line.')
            system.servePatient()
        elif (inp == 4):
            flag = system.canDocGoHome()
            if (flag == True):
                print("Yes. No more patient remaining, hasta la vista")
            else:
                print("NO. Patients still waiting for the doctor.\n")
        elif (inp == 3):
            system.cancelAll()
            print("All appointments has been cancelled!")
        else:
            print("Thank you for your visit. GoodBye !")
            break


main()
