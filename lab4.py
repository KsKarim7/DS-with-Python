# https://docs.google.com/document/d/19f_lVAgsnCHkvk6SrJ4MmZMyGauLnADsyxON711bex0/edit?usp=drive_link

class Patient:
    def __init__(self, id, name, age, bgrp, n, p):
        count = 0
        if (count == 0):
            self.id = 1
            count += 1
        else:
            self.id = id+1
        self.name = name
        self.age = age
        self.bgrp = bgrp
        self.next = n
        self.prev = p


class WRM:
    def __init__(self):
        self.dp = Patient(None, None, None, None, None)
        self.dp.next = self.dp
        self.prev = self.dp
        self.tail = self.dp

    def RegisterPatient(self, id, name, age, bloodgroup):
        node = Patient(id, name, age, bloodgroup, self.dp, self.tail)
        self.tail.next = node
        self.tail = self.tail.next
        self.dp.prev = self.tail

    def servePatient(self):
        node = self.dp.next
        prev = node.prev
        nex = node.next
        prev.next = nex
        nex.prev = prev

    def cancelAll(self):
        self.dp.next = self.dp
        self.dp.prev = self.dp

    def canDocGoHome(self):
        if (self.dp.next == self.dp):
            return True
        else:
            return False

    def showAllpatient(self):
        temp = self.dh.next
        while (temp != self.dh):
            print(
                f'Patient {temp.id}: Name: {temp.name}  Age: {temp.age} Blood Group: {temp.bgrp}')

    def reverseTheLine(self):
        pass
