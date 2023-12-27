import sys
import random
from enum import Enum
import time

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


# print(RPS(2))
# print(RPS.ROCK)
# print(RPS['ROCK'])
# print(RPS.ROCK.value)

playagain = True
while playagain:
    print(" ")
    playerchoice = input("\nEnter...\n1 for rock,\n2 for paper, or \n3 for scissors:\n\n ")

    player = int(playerchoice)

    if player < 1 or player > 3:
        sys.exit("You must enter 1, 2 or 3. ")


    computerchoice = random.choice("123") # Str ver.

    computer = int(computerchoice) # Int ver.

    print(" ")
    print("You chose " + str(RPS(player)).replace('RPS.', ' ') + ".")
    print("Python chose " + str(RPS(computer)).replace('RPS.', ' ') + ".")
    print(" ")

    playerwin = ("you won.")
    compwin = ("Python won.")
    tie = ("You both tied.")
    
    if player == 1 and computer == 3:
        print("🎉 " + playerwin.center(20, "="))
    elif player == 2 and computer == 1:
        print("🎉 " + playerwin.center(20, "="))
    elif player == 3 and computer == 2:
        print("🎉 " + playerwin.center(20, "=")) 
    elif player == computer:
        print("😐 " + tie.center(20, "="))
    else:
        print("😞 " + compwin.center(20, "="))

    playagain = input("\nPlay again? \nY for Yes or \nQ to Quit \n\n")

    if playagain.lower() == "y":
        continue
    else:
        print("\n🎉🎉🎉🎉")
        print("Thank you for playing!\n")
        playagain = False
sys.exit("Bye! 👋")

        