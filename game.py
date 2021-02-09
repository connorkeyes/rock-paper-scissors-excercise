# game.py

import random

line = "-------------------"

username = input("Please enter your name:")
question = input(f"Welcome, {username}, to my rock paper scissors game! Would you like to play?")

if question == str.casefold("Yes"):
    print("Awesome! Let's do it!")
    print(line)
    print(line)

elif question == str.casefold("No"):
    print("Fine, be that way. Jerk.")
    exit()

else:
    print("I'm not sure what you're saying. Please answer yes or no.")
    exit()

comp_move = random.choice(["Rock", "Paper", "Scissors"])
user_move = input("Rock, Paper, Scissors, Shoot! ")

print("Your move:", user_move)
print("My move:", comp_move)

comp_win = "You lose! Loser!"
user_win = "I lose! Dang it!"
tie = "It's a tie!"

if user_move == str.casefold("Rock"):
    if comp_move == "Rock":
        print(tie)
    if comp_move == "Paper":
        print(comp_win)
    if comp_move == "Scissors":
        print(user_win)

elif user_move == str.casefold("Paper"):
    if comp_move == "Rock":
        print(user_win)
    if comp_move == "Paper":
        print(tie)
    if comp_move == "Scissors":
        print(comp_win)

elif user_move == str.casefold("Scissors"):
    if comp_move == "Rock":
        print(comp_win)
    if comp_move == "Paper":
        print(user_win)
    if comp_move == "Scissors":
        print(tie)

else:
    print("Something went wrong. Please enter rock, paper, or scissors as your move.")
    exit()