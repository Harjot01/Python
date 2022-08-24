print('''To generate a table of random number or number entered by the user''')
import random
while True:
    user_input = input("Do you want table of random number(rn) or custom number(cn)? (rn/cn)").casefold()
    if user_input == "rn":
        comp = random.randint(1, 100)
        for i in range(1, 11):
            print(f"{comp} x {i} = {comp*i}")
    
    elif user_input ==  "cn":
        number = int(input("Ok table of which number do you want?"))
        for i in range(1, 11):
            print(f"{number} x {i} = {number*i}")
