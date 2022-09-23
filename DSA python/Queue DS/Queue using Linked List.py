import os

class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def NodeExists(self, key):
        exists = False
        ptr = self.front
        while ptr is not None:
            if ptr.key == key:
                exists = True
                break
            ptr = ptr.next
        return exists

    def isEmpty(self):
        if self.front == self.rear == None:
            return True
        else:
            return False

    def Enqueue(self, n):
        if self.isEmpty():
            self.rear = n
            self.front = n
            print("Node Enqueued")
        elif self.NodeExists(n.key):
            print("Node already exists with the key value of ", n.key)
        else:
            self.rear.next = n
            self.rear = n
            print("Node Enqueued")

    def Dequeue(self):
        temp = None
        if self.isEmpty():
            print("Queue is Empty")
        elif self.front == self.rear:
            temp = self.front
            self.front = self.rear = None
        else:
            temp = self.front
            self.front = self.front.next

        return temp

    def Count(self):
        ct = 0
        ptr = self.front
        while ptr is not None:
            ct += 1
            ptr = ptr.next
        return ct

    def Display(self):
        if (self.isEmpty()):
            print("Queue is Empty")
        else:
            ptr = self.front
            while ptr is not None:
                print("(" + str(ptr.key) + ", " + str(ptr.data) + ") --> ", end="")
                ptr = ptr.next
            print("")


obj = Queue()
while 1:
    print("What operation do you want to perform? Select Option number. Enter 0 to exit.")
    print("1. Enqueue()")
    print("2. Dequeue()")
    print("3. isEmpty()")
    print("4. count()")
    print("5. display()")
    print("6. Clear Screen")

    option = int(input())

    if option == 0:
        break
    elif option == 1:
        print("Enqueue Function Called...")
        key = int(input("Enter the key: "))
        data = int(input("Enter the data: "))
        n = Node(key, data)
        n.key = key
        n.data = data
        obj.Enqueue(n)
    elif option == 2:
        print("Dequeue Function Called...")
        temp = obj.Dequeue()
        print("Dequeued Node: " + "(" + str(temp.key) + ", " + str(temp.data) + ")")
    elif option == 3:
        print("isEmpty Function Called...")
        if obj.isEmpty():
            print("Queue is Empty")
        else:
            print("Queue is not Empty")
    elif option == 4:
        print("Count Function Called...")
        print("The total elements inside the Queue are ", obj.Count())
    elif option == 5:
        print("Display Function Called...")
        obj.Display()
    elif option == 6:
        os.system('clear')
    else:
        print("Enter proper option number")
