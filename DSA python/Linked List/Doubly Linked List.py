import os
class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.prev = None
        self.next = None


class DLinkedList:
    def __init__(self):
        self.head = None

    def NodeExists(self, key):
        temp = None
        ptr = self.head
        while ptr is not None:
            if (ptr.key == key):
                temp = ptr
                break
            ptr = ptr.next
        return temp

    def AppendNode(self, n):
        if (self.NodeExists(n.key) != None):
            print("Node already exists with the key value of ", n.key)
        else:
            if (self.head == None):
                self.head = n
                n.prev = self.head
                print("Node Appended")
            else:
                ptr = self.head
                while ptr.next is not None:
                    ptr = ptr.next
                ptr.next = n
                n.prev = ptr
                print("Node Appended")

    def PrependNode(self, n):
        if (self.NodeExists(n.key) != None):
            print("Node already exists with the key value of ", n.key)
        else:
            if (self.head == None):
                self.head = n
                print("Node Prepended")

            else:
                n.next = self.head
                self.head.prev = n
                self.head = n
                print("Node Prepended")

    def InsertNodeAfter(self, n, key):
        ptr = self.NodeExists(key)
        if (ptr == None):
            print("No node exists with the key value of ", key)
        else:
            if (self.NodeExists(n.key) != None):
                print("Node already exists with the key value of ", n.key)
            else:
                if (ptr.next == None):
                    ptr.next = n
                    n.prev = ptr
                    print("Node Inserted")
                else:
                    n.next = ptr.next
                    ptr.next.prev = n
                    n.prev = ptr
                    ptr.next = n
                    print("Node Inserted")

    def InsertNodeBefore(self, n, key):
        ptr = self.NodeExists(key)
        if (ptr == None):
            print("No node exists with the key value of ", key)
        else:
            if (self.NodeExists(n.key) != None):
                print("Node already exists with the key value of ", n.key)
            else:
                if (ptr == self.head):
                    ptr.prev = n
                    n.next = ptr
                    self.head = n
                    print("Node Inserted")
                else:
                    ptr.prev.next = n
                    n.prev = ptr.prev
                    n.next = ptr
                    ptr.prev = n
                    print("Node Inserted")

    def DeleteNode(self, key):
        ptr = self.NodeExists(key)
        if (ptr == None):
            print("No node exists with the key value of ", key)
        else:
            if (ptr == self.head):
                self.head = self.head.next
                print("Node Deleted")
            else:
                if (ptr.next == None):
                    ptr.prev.next = None
                    print("Node Deleted")

                else:
                    ptr.prev.next = ptr.next
                    ptr.next.prev = ptr.prev
                    ptr.next = ptr.prev = None
                    print("Node Deleted")

    def UpdateNode(self, key, data):
        ptr = self.NodeExists(key)
        if(ptr == None):
            print("No node exists with the key value of ", key)
        else:
            ptr.data = data
            print("Node Updated Successfully")

    def Display(self):
        printval = self.head
        while printval is not None:
            print("(" + str(printval.key) + ", " +
                  str(printval.data) + ")" + " <--> ", end="")
            printval = printval.next
        print("")


d = DLinkedList()
while (True):
    print("0. Exit")
    print("1. Append()")
    print("2. Prepend()")
    print("3. InsertNodeAfter()")
    print("4. InsertNodeBefore()")
    print("5. DeleteNode()")
    print("6. UpdateNode()")
    print("7. Display()")
    print("8. Clear Screen")

    option = int(input("Enter Your Choice\n"))
    if (option == 0):
        print("GoodBye...")
        break
    elif (option == 1):
        print("Append Function Called...")
        key = int(input("Enter the key\n"))
        data = int(input("Enter the data\n"))
        n = Node(key, data)
        d.AppendNode(n)
    elif (option == 2):
        print("Prepend Function Called...")
        key = int(input("Enter the key\n"))
        data = int(input("Enter the data\n"))
        n = Node(key, data)
        d.PrependNode(n)
    elif (option == 3):
        print("InsertNodeAfter function Called...")
        k = int(input("Enter the key where you want to Insert\n"))
        key = int(input("Enter the key of the node\n"))
        data = int(input("Enter the data of the node\n"))
        n = Node(key, data)
        d.InsertNodeAfter(n, k)
    elif (option == 4):
        print("InsertNodeBefore function Called...")
        k = int(input("Enter the key where you want to Insert\n"))
        key = int(input("Enter the key of the node\n"))
        data = int(input("Enter the data of the node\n"))
        n = Node(key, data)
        d.InsertNodeBefore(n, k)
    elif (option == 5):
        print("DeleteNode function Called...")
        key = int(input("Enter the key\n"))
        d.DeleteNode(key)
    elif (option == 6):
        print("UpdateNode Function Called...")
        key = int(input("Enter the key\n"))
        data = int(input("Enter the data\n"))
        d.UpdateNode(key, data)

    elif (option == 7):
        print("Display Function Called...")
        d.Display()
    elif (option == 8):
        os.system('clear')

    else:
        print("Invalid Option, Try Again!!!")
