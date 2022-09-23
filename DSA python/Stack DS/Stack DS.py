# You can only get smarter by playing a smarter opponent 
import os
class Stack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__top = -1
        self.arr = [0] * capacity

    def isEmpty(self):
        if (self.__top == -1):
            return True
        else:
            return False 

    def isFull(self):
        if (self.__top == self.__capacity - 1):
            return True
        else:
            return False

    def Push(self, elt):
        if (self.isFull()):
            print("Stack Overflow")
        else:
            self.__top += 1
            self.arr[self.__top] = elt
            print("Element pushed inside the Stack")

    def Pop(self):
        x = 0
        if (self.isEmpty()):
            print("Stack Underflow")
        else:
            x = self.arr[self.__top]
            self.arr[self.__top] = 0
            self.__top -= 1
        return x

    def Change(self, index, value):
        if (index >= 0 and index < self.__capacity):
            self.arr[index] = value
            print("Value changed at index " + str(index))
        else:
            print("Invalid Index")

    def Peek(self, index):
        if (index >= 0 and index < self.__capacity):
            return self.arr[index]
        else:
            print("Invalid Index")

    def Count(self):
        return self.__top + 1

    def Display(self):
        print("Displaying all the values inside the Stack")
        for i in reversed(range(self.__capacity)):
            print(" -----")
            print(" " + "| " + str(self.arr[i]) + " |")
        print(" -----")


size = int(input("Enter the size of the Stack\n"))
s = Stack(size)

while (True):
    print("0. Exit")
    print("1. Push()")
    print("2. Pop()")
    print("3. isEmpty()")
    print("4. isFull()")
    print("5. peek()")
    print("6. count()")
    print("7. change()")
    print("8. display()")
    print("9. Clear Screen")

    option = int(input("Enter Your Choice\n"))
    if (option == 0):
        print("GoodBye...")
        break
    elif (option == 1):
        print("Push Function Called...")
        elt = int(input("Enter the element to push in the Stack\n"))
        s.Push(elt)
    elif (option == 2):
        print("Pop Function Called...")
        s.Pop()
    elif (option == 3):
        print("isEmpty function Called...")
        if (s.isEmpty()):
            print("Stack is Empty")
        else:
            print("Stack is not Empty")
    elif (option == 4):
        print("isFull Function Called...")
        if (s.isFull()):
            print("Stack is Full")
        else:
            print("Stack is not Full")
    elif (option == 5):
        print("Peek Function Called...")
        idx = int(input("Enter the index position\n"))
        print("The value at index " + str(idx) + " is " + str(s.Peek(idx)))
    elif (option == 6):
        print("Count Function Called...")
        print("The total elements in the Stack are " + str(s.Count()))
    elif (option == 7):
        print("Change Function Called...")
        idx = int(input("Enter a index at which you want to change the value\n"))
        elt = int(input("Enter the value that you want to change\n"))
        s.Change(idx, elt)
    elif (option == 8):
        print("Display Function Called...")
        s.Display()
    elif (option == 9):
        os.system('clear')

    else:
        print("Invalid Option, Try Again!!!")
