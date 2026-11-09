'''
WORKFLOW OF PROJECT 

1) INPUT FROM USER(ROCK,PAPER,SCISSOR)
2) COMPUTER CHOICE(COMPUTER WILL CHOOSE RANDOMLY NOT CONDITIONALLY)
3) RESULT PRINT 


CASES:
A - ROCK
ROCK-> ROCK = TIE
ROCK -> PAPER = PAPER WIN
ROCK -> SCISSOR = ROCK WINE

B-PAPER
PAPER -> PAPER = TIE
PAPER -> ROCK = PAPER WIN
PAPER -> SCISSOR = SCISSOR WIN

C-SCISSOR
SCISSOR -> SCISSOR = TIE
SCISSOR -> ROCK = ROCK WIN
SCISSOR -> PAPER = SCISSOR WIN

'''

import random
item_list = ["Rock","Paper","Scissor"]

user_choice = input("Enter your move : ")
comp_choice = random.choice(item_list) 
print(f"User Choice = {user_choice}, Computer Choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both are same := Match Ties")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper Covers Rock := Computer Wins")
    else:
        print("Rock Smashes Scissor := User Wins")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor Cuts Paper := Computer Wins")
    else:
        print("Paper Covers Rock := User Wins")

elif user_choice == "Scissor":
     if comp_choice == "Rock":
        print("Rock Smashes Scissor := Computer Wins")
     else:
        print("Scissor Cuts Paper := User Wins")       






