output = 0
print(output)

while True:
    sign = input()
    num = int(input("Enter the number: "))
    if sign == "+":
        output += num

    elif sign == "-":
        output -= num

    elif sign == "*":
        output *= num

    elif sign == "/":
        output /= num

    elif sign == "//":
        output //= num
        
    elif sign == "%":
        output %= num

    elif sign == "**":
        output **= num
    print("output is ", output)
