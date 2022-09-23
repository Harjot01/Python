from inspect import isfunction
import os


class Queue:
    def __init__(self, capacity):
        self.__front = -1
        self.__rear = -1
        self.__capacity = capacity
        self.__arr = [0] * self.__capacity

    def isEmpty(self):
        if self.__front == -1 and self.__rear == -1:
            return True
        else:
            return False

    def isFull(self):
        if self.__front == 0 and self.__rear == self.__capacity - 1:
            return True
        else:
            return False

    def Enqueue(self, value):
        if self.isFull():
            print("Queue is Full")
            return
        elif self.isEmpty():
            self.__front = self.__rear = 0
            self.__arr[self.__rear] = value
            return value
        else:
            self.__rear += 1
            self.__arr[self.__rear] = value
            return value

    def Dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        elif self.__front == self.__rear:
            x = self.__arr[self.__front]
            self.__arr[self.__front] = 0
            self.__front = self.__rear = -1
            return x
        else:
            x = self.__arr[self.__front]
            self.__arr[self.__front] = 0
            self.__front += 1
            return x

    def Display(self):
        print("Displaying all the values inside the Queue")
        for i in range(self.__capacity):
            print(self.__arr[i], end=" ")
        print("")

    def Count(self):
        return (self.__rear - self.__front + 1)


capacity = int(input("Enter the capacity of the Queue\n"))
obj = Queue(capacity)

while 1:
    print("What operation do you want to perform? Select Option number. Enter 0 to exit.")
    print("1. Enqueue()")
    print("2. Dequeue()")
    print("3. isEmpty()")
    print("4. isFull()")
    print("5. count()")
    print("6. display()")
    print("7. Clear Screen")

    option = int(input())

    if option == 0:
        break
    elif option == 1:
        print("Enqueue Function Called...")
        elt = int(input("Enter the element you want to enqueue: "))
        print("Enqueued value: ", obj.Enqueue(elt))
    elif option == 2:
        print("Dequeue Function Called...")
        print("Dequeued value: ", obj.Dequeue())
    elif option == 3:
        print("isEmpty Function Called...")
        if obj.isEmpty():
            print("Queue is Empty")
        else:
            print("Queue is not Empty")
    elif option == 4:
        print("isFull Function Called...")
        if obj.isFull():
            print("Queue is Full")
        else:
            print("Queue is not Full")
    elif option == 5:
        print("Count Function Called...")
        print("The total elements inside the Queue are ", obj.Count())
    elif option == 6:
        print("Display Function Called...")
        obj.Display()
    elif option == 7:
        os.system('clear')
    else:
        print("Enter proper option number")
