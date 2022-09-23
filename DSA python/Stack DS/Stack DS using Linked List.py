import os


class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def NodeExists(self, key):
        exists = None
        ptr = self.top
        while ptr is not None:
            if (ptr.key == key):
                exists = ptr
                break
            ptr = ptr.next
        return exists

    def isEmpty(self):
        if (self.top == None):
            return True
        else:
            return False

    def Push(self, n):
        if (self.NodeExists(n.key) != None):
            print("Node already exists with the key value of ", n.key)
        else:
            if (self.top == None):
                self.top = n
                print("Node Pushed inside Stack")
            else:
                temp = self.top
                self.top = n
                n.next = temp
                print("Node Pushed inside Stack")

    def Pop(self):
        temp = None
        if (self.isEmpty()):
            print("Stack Underflow")
        else:
            temp = self.top
            self.top = self.top.next
        return temp

    def Peek(self, key):
        ptr = self.NodeExists(key)
        if (ptr == None):
            print("No node exists with the key value of ", key)
        else:
            print("The value at key " + str(key) + " is " + str(ptr.data))

    def Change(self, key, data):
        ptr = self.NodeExists(key)
        if (ptr == None):
            print("No node exists with the key value of ", key)
        else:
            ptr.data = data
            print("Updated Successfully")

    def Count(self):
        ct = 0
        ptr = self.top
        while ptr is not None:
            ct += 1
            ptr = ptr.next
        return ct

    def Display(self):
        ptr = self.top
        print("------")
        while ptr is not None:
            print("(" + str(ptr.key) + ", " + str(ptr.data) + ")")
            print("------")
            ptr = ptr.next


s = Stack()
while (True):
    print("0. Exit")
    print("1. Push()")
    print("2. Pop()")
    print("3. isEmpty()")
    print("4. peek()")
    print("5. count()")
    print("6. change()")
    print("7. display()")
    print("8. Clear Screen")

    option = int(input("Enter Your Choice\n"))
    if (option == 0):
        print("GoodBye...")
        break
    elif (option == 1):
        print("Push Function Called...")
        key = int(input("Enter the key\n"))
        data = int(input("Enter the data\n"))
        n = Node(key, data)
        s.Push(n)
    elif (option == 2):
        print("Pop Function Called...")
        print("Successfully Poped out ", s.Pop())
    elif (option == 3):
        print("isEmpty function Called...")
        if (s.isEmpty()):
            print("Stack is Empty")
        else:
            print("Stack is not Empty")

    elif (option == 4):
        print("Peek Function Called...")
        key = int(input("Enter the key position\n"))
        print("The value at index " + str(key) + " is " + str(s.Peek(key)))
    elif (option == 5):
        print("Count Function Called...")
        print("The total elements in the Stack are " + str(s.Count()))
    elif (option == 6):
        print("Change Function Called...")
        key = int(input("Enter a key at which you want to change the value\n"))
        elt = int(input("Enter the value that you want to change\n"))
        s.Change(key, elt)
    elif (option == 7):
        print("Display Function Called...")
        s.Display()
    elif (option == 8):
        os.system('clear')

    else:
        print("Invalid Option, Try Again!!!")
