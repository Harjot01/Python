import os
class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None


class CLinkedList:
    def __init__(self):
        self.head = None

    def NodeExists(self, key):
        exists = None
        ptr = self.head
        while 1:
            if (ptr.key == key):
                exists = ptr
                break
            ptr = ptr.next
            if (ptr == self.head):
                break
        return exists

    def AppendNode(self, n):
        if (self.head == None):
            self.head = n
            n.next = self.head
            print("Node Appended")
        else:
            if (self.NodeExists(n.key) != None):
                print("Node already exists with the key value of ", n.key)
            else:
                print("Node Appended at last")
                ptr = self.head
                while ptr.next is not self.head:
                    ptr = ptr.next
                ptr.next = n
                n.next = self.head

    def PrependNode(self, n):
        if (self.head == None):
            self.head = n
            n.next = self.head
            print("Node Prepended")
        else:
            if (self.NodeExists(n.key) != None):
                print("Node already exists with the key value of ", n.key)
            else:
                ptr = self.head
                while ptr.next is not self.head:
                    ptr = ptr.next
                n.next = self.head
                self.head = n
                ptr.next = n
                print("Node Prepended")

    def InsertNodeAfter(self, n, key):
        ptr = self.NodeExists(key)
        if (ptr == None):
            print("No node exists with the key value of ", key)
        else:
            if (self.NodeExists(n.key) != None):
                print("Node already exists with the key value of ", n.key)
            else:
                if (ptr.next == self.head):
                    ptr.next = n
                    n.next = self.head
                    print("Node Inserted")
                else:
                    n.next = ptr.next
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
                    while 1:
                        ptr = ptr.next
                        if (ptr.next == self.head):
                            break
                    n.next = self.head
                    self.head = n
                    ptr.next = n
                    print("Node Inserted")
                else:
                    prev_ptr = self.head
                    curr_ptr = prev_ptr.next
                    while curr_ptr is not self.head:
                        if (curr_ptr.key == key):
                            break
                        prev_ptr = prev_ptr.next
                        curr_ptr = curr_ptr.next
                    n.next = prev_ptr.next
                    prev_ptr.next = n
                    print("Node Inserted")

    def DeleteNode(self, key):
        if(self.head == None):
            print("No nodes in the Linked List")
        else:
            if(self.head.key == key):
                if(self.head.next == self.head):
                    self.head = None
                    print("Node Deleted")
                else:
                    ptr = self.head
                    while ptr.next is not self.head:
                        ptr = ptr.next
                    self.head = self.head.next
                    ptr.next = self.head
                    print("Node Deleted")
            else:
                prev_ptr = self.head
                curr_ptr = prev_ptr.next
                while curr_ptr is not self.head:
                    if(curr_ptr.key == key):
                        break
                    prev_ptr = prev_ptr.next
                    curr_ptr = curr_ptr.next
                
                if(curr_ptr is self.head):
                    print("No node exists with the key value of ", key)
                else:
                    prev_ptr.next = curr_ptr.next
                    curr_ptr.next = None
                    print("Node Deleted")

    def UpdateNode(self, key, data):
        ptr = self.NodeExists(key)
        if(ptr == None):
            print("No node exists with the key value of ", key)
        else:
            ptr.data = data
            print("Node Updated")


    def Display(self):
        ptr = self.head
        while 1:
            print("(" + str(ptr.key) + ", " +
                  str(ptr.data) + ")" + " --> ", end="")
            ptr = ptr.next
            if (ptr == self.head):
                break
        print("")


c = CLinkedList()
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
        c.AppendNode(n)
    elif (option == 2):
        print("Prepend Function Called...")
        key = int(input("Enter the key\n"))
        data = int(input("Enter the data\n"))
        n = Node(key, data)
        c.PrependNode(n)
    elif (option == 3):
        print("InsertNodeAfter function Called...")
        k = int(input("Enter the key where you want to Insert\n"))
        key = int(input("Enter the key of the node\n"))
        data = int(input("Enter the data of the node\n"))
        n = Node(key, data)
        c.InsertNodeAfter(n, k)
    elif (option == 4):
        print("InsertNodeBefore function Called...")
        k = int(input("Enter the key where you want to Insert\n"))
        key = int(input("Enter the key of the node\n"))
        data = int(input("Enter the data of the node\n"))
        n = Node(key, data)
        c.InsertNodeBefore(n, k)
    elif (option == 5):
        print("DeleteNode function Called...")
        key = int(input("Enter the key\n"))
        c.DeleteNode(key)
    elif (option == 6):
        print("UpdateNode Function Called...")
        key = int(input("Enter the key\n"))
        data = int(input("Enter the data\n"))
        c.UpdateNode(key, data)

    elif (option == 7):
        print("Display Function Called...")
        c.Display()
    elif (option == 8):
        os.system('clear')

    else:
        print("Invalid Option, Try Again!!!")
