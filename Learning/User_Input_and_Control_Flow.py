import sys
import random
from enum import Enum


print("User_Input_and_Control_Flow")


class GameConfig(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print("================")
playerchoice = int(input("Press...\n1 for Rock,\n2 for Paper \n3 for Scissors:\n\n"))

player = int(playerchoice)

if playerchoice < 1 or playerchoice > 3:
    sys.exit("You must enter 1, 2, or 3.")

computerchoice = int(random.choice("123"))

computer = int(computerchoice)

print("================")
print("You chose " + str(GameConfig(playerchoice)).replace("GameConfig.", "") + ".")
print(
    "Python chose " + str(GameConfig(computerchoice)).replace("GameConfig.", "") + "."
)
print("================")

if playerchoice == 1 and computerchoice == 3:
    print("🎉 You win!")
elif playerchoice == 2 and computerchoice == 1:
    print("🎉 You win!")
elif playerchoice == 3 and computerchoice == 2:
    print("🎉 You win!")
elif playerchoice == computerchoice:
    print("😲 Tie game!")
else:
    print("🐍 Python wins!")
