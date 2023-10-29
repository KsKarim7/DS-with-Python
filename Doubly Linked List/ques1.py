
class node:
    def __init__(self, elem, next, prev):
        self.elem = elem
        self.next = next
        self.prev = prev


def insert_list(head, tail, val):
    newNode = node(val, None, None)
    if (tail == None):
        head = newNode
        tail = newNode
        return
    tail.next = newNode
    newNode.prev = tail
    tail = tail.next


def print_list(head):
    temp = head
    while (temp != None):
        print(temp.elem, " ")
        temp = temp.next
    print()


def check_palindrome(head, tail, flag):
    tempH = head
    tempT = tail
    while (tempH != None):
        if (tempH.elem != tempT.elem):
            flag = False
            break
        tempH = tempH.next
        tempT = tempT.prev


head = None
tail = None
flag = True
while (True):
    inp = int(input())
    if (inp == -1):
        break
    insert_list(head, tail, inp)
print_list(head)
