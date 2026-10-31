#Dice-Rolling-Simulator
import random

while True:
    roll = input("Roll the dice? (yes/no): ")

    if roll.lower() == "yes":
        number = random.randint(1, 6)
        print("You rolled:", number)

    elif roll.lower() == "no":
        print("Thanks for playing!")
        break

    else:
        print("Please enter yes or no.")
