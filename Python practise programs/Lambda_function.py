addition = lambda a, b:a+b
subtraction = lambda a, b:a-b
multiplication = lambda a, b:a*b
division = lambda a, b:a/b
square = lambda a: a**2

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
print(addition(x, y))
print(subtraction(x, y))
print(multiplication(x, y))
print(division(x, y))
print(square(4))