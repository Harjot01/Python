import os


class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None

    def NodeExists(self, key):
        exists = None
        ptr = self.head
        while ptr is not None:
            if (ptr.key == key):
                exists = ptr
            ptr = ptr.next
        return exists

    def AppendNode(self, n):
        if (self.head == None):
            self.head = n
            print("Node Appended")
        else:
            if (self.NodeExists(n.key) != None):
                print("Node already exists with the key value ", n.key)
            else:
                ptr = self.head
                while ptr.next is not None:
                    ptr = ptr.next
                ptr.next = n
                print("Node Appended")

    def PrependNode(self, n):
        if (self.NodeExists(n.key) != None):
            print("Node already exists with the key value " + n.key)
        else:
            if (self.head == None):
                self.head = n
                print("Node Prepended")
            else:
                n.next = self.head
                self.head = n
                print("Node Prepended")

    def InsertNodeAfter(self, n, key):
        ptr = self.NodeExists(key)
        if (ptr == None):
            print("No node exists with the key ", key)
        else:
            if (self.NodeExists(n.key) != None):
                print("Node already exists with the key value " + n.key)
            else:
                n.next = ptr.next
                ptr.next = n
                print("Node Inserted")

    def DeleteNode(self, key):
        if (self.head == None):
            print("List is Empty, so cannot delete any nodes")
        else:
            if (self.head.key == key):
                self.head = self.head.next
                print("Node Deleted Successfully")

            else:
                temp = None
                prev_ptr = self.head
                curr_ptr = prev_ptr.next
                while curr_ptr is not None:
                    if (curr_ptr.key == key):
                        temp = curr_ptr
                        curr_ptr = None
                    else:
                        prev_ptr = prev_ptr.next
                        curr_ptr = curr_ptr.next
                if (temp == None):
                    print("No node exists with the key value of ", key)
                else:
                    prev_ptr.next = temp.next
                    temp.next = None
                    print("Node Deleted Successfully")

    def InsertNodeBefore(self, n, key):
        if (self.NodeExists(n.key) != None):
            print("Node already exists with the key value " + n.key)

        else:
            if (self.head.key == key):
                n.next = self.head
                self.head = n
                print("Node Inserted")
            else:
                temp = None
                prev_ptr = self.head
                curr_ptr = prev_ptr.next
                while curr_ptr is not None:
                    if (curr_ptr.key == key):
                        temp = curr_ptr
                        curr_ptr = None
                    else:
                        prev_ptr = prev_ptr.next
                        curr_ptr = curr_ptr.next
                if (temp == None):
                    print("No node exists with the key value ", key)
                else:
                    n.next = prev_ptr.next
                    prev_ptr.next = n
                    print("Node Inserted")

    def UpdateNode(self, key, data):
        ptr = self.NodeExists(key)
        if (ptr == None):
            print("No node exists with the key value ", key)
        else:
            ptr.data = data
            print("Node Updated")

    def Display(self):
        printval = self.head
        while printval is not None:
            print("(" + str(printval.key) + ", " +
                  str(printval.data) + ")" + " --> ", end="")
            printval = printval.next
        print("")


s = SLinkedList()
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
        s.AppendNode(n)
    elif (option == 2):
        print("Prepend Function Called...")
        key = int(input("Enter the key\n"))
        data = int(input("Enter the data\n"))
        n = Node(key, data)
        s.PrependNode(n)
    elif (option == 3):
        print("InsertNodeAfter function Called...")
        k = int(input("Enter the key where you want to Insert\n"))
        key = int(input("Enter the key of the node\n"))
        data = int(input("Enter the data of the node\n"))
        n = Node(key, data)
        s.InsertNodeAfter(n, k)
    elif (option == 4):
        print("InsertNodeBefore function Called...")
        k = int(input("Enter the key where you want to Insert\n"))
        key = int(input("Enter the key of the node\n"))
        data = int(input("Enter the data of the node\n"))
        n = Node(key, data)
        s.InsertNodeBefore(n, k)
    elif (option == 5):
        print("DeleteNode function Called...")
        key = int(input("Enter the key\n"))
        s.DeleteNode(key)
    elif (option == 6):
        print("UpdateNode Function Called...")
        key = int(input("Enter the key\n"))
        data = int(input("Enter the data\n"))
        s.UpdateNode(key, data)

    elif (option == 7):
        print("Display Function Called...")
        s.Display()
    elif (option == 8):
        os.system('clear')

    else:
        print("Invalid Option, Try Again!!!")
