# game.py

import random

line = "-------------------"

username = input("Please enter your name:")
question = input(f"Welcome, {username}, to my rock paper scissors game! Would you like to play?")
if question == str.casefold("Yes"):
    print("Awesome! Let's do it!")
    print(line) * 2
elif question == str.casefold("No"):
    print("Fine, be that way. Jerk.")
    exit()

comp_move = random.choice(["Rock", "Paper", "Scissors"])
user_move = input("Rock, Paper, Scissors, Shoot!")
print("Your move:", user_move)
print("My move:", comp_move)
if user_move == "Rock":
    if comp_move == "Rock":
        print("It's a tie!")
    if comp_move == "Paper":
        print("You lose! Loser!")
    if comp_move == "Scissors":
        print("I lose! Dang it!")
elif comp_move == "Paper":
    if comp_move == "Rock":
        print("It's a tie!")
    if comp_move == "Paper"
        print("You lose! Loser!")
    if comp_move == "Scissors"
        print("I lose! Dang it!")