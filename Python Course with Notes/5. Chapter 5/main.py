#importing ramdom module
import random
#printing the title
print("Snake[s]-Water[w]-Gun[g]")
print("Hi i am a computer and i will play this game with you")
print("Keep these rules in your mind",end=" ")
print("to type Snake enter s, to type Water enter w and to type Gun enter g")

no_of_rounds = int(input("Enter the no of rounds\n"))


#game_functions
game_functions = ["s", "w", "g"]

#initialising rounds
rounds = 1

#computer's wins
comp_win = 0

#person wins
you_win = 0





while rounds <= no_of_rounds:
    #Displaying rounds
    print(f"Round :{rounds}\nSnake - 's'\nWater - 'w'\nGun - 'g'")
    

     # Exception handling
    try:
        you = input("Chose your option: ")
    except EOFError as e:
        print(e)

    # Control of bad inputs
    if you != 's' and you!= 'w' and you != 'g':
        print("Invalid input, try again\n")
        continue
 

    #Computer's turn
    print("Computer - I have chosen")
    comp = random.choice(game_functions)
    

    
    #displaying the outputs
    print("You chose", you)
    print("Computer chose", comp)

    # Conditions based on the game rule
    if comp == 's':
        if you == 'w':
            comp_win += 1
        elif you == 'g':
            you_win += 1
 
    elif comp == 'w':
        if you == 'g':
            comp_win += 1
        elif you == 's':
            you_win += 1
 
    elif comp == 'g':
        if you == 's':
            comp_win += 1
        elif you == 'w':
            you_win += 1
  

    # Winner of every round
    if you_win > comp_win:
        print(f"You won round{rounds}\n")
    elif comp_win > you_win:
        print(f"Computer won round {rounds}\n")
    else:
        print("Draw!!\n")

    rounds+=1


# game win
if you_win > comp_win:
    print("Congratulations!! You won")
elif comp_win > you_win:
    print("You lose!")
else:
    print("Match draw!!")