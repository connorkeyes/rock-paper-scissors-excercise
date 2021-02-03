# game.py

import random

line = "-----------------"

username = input("Please enter your name:")
question = input("Welcome, " + username + ", to my rock paper scissors game! Would you like to play?")
if question == str.casefold("Yes"):
    print("Awesome! Let's do it!")
    print(line) * 2
elif question == str.casefold("No"):
    print("Fine, be that way then. Jerk.")
    exit()

while True:
    comp_move = random.choice(["Rock", "Paper", "Scissors"])
    inp = input("Rock, Paper, Scissors, Shoot!")
    print("Your move:", inp)
    print("My move:", comp_move)
    if inp == "Rock":
        if comp_move == "Rock":
            print("It's a tie!")
        if comp_move == "Paper"
            print("You lose! Loser!")
        if comp_move == "Scissors"
            print("I lose! Dang it!")
    elif inp == "Paper":
        if comp_move == "Rock":
            print("It's a tie!")
        if comp_move == "Paper"
            print("You lose! Loser!")
        if comp_move == "Scissors"
            print("I lose! Dang it!")
    
    