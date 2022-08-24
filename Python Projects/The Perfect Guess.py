
print("****************************The Perfect Guess**********************************")
print("Here are some GAME RULES")
print("You have to guess a number between 1 and 10")
print("You will get 8 chances to guess the number")
print("Every invalid input will be counted and number of chances will reduce accordingly")

import random
user_chances = 1
user_input = input("Do you want to continue? (y/n)")
if user_input == "y":
    name = input("To continue enter your name\n").capitalize()
    print(f"Ok get ready {name}")
    while user_chances <= 8:
        try:
            my_chance = random.randint(1,21)
            guess = int(input("Enter you number\n"))
        
            if guess > my_chance:
                print("Lower number please")
            
            elif guess < my_chance:
                print("Higher number please")

            elif guess == my_chance:
                print(f"{name} you guessed it right!!")
                print("The number of chances you took are: ", user_chances)
                break
        except Exception as e:
            print("Invalid Input")
        user_chances += 1
    if user_chances > 8:
        print(f"Oops {name} you ran out of chances!!")
    # with open("hiscore.txt") as f:
    #     hiscore = int(f.read()) 
    
    # if user_chances < hiscore:
    #     print("You have just broken the high score!")
    #     with open("hiscore.txt", "w") as f:
    #         f.write(str(user_chances))
    
elif user_input == "n":
    print(f"Okay, np have a nice day!!")

else:
    print("Invalid Input")