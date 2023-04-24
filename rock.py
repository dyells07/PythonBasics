import random
import codecs
import sys
import os

if sys.stdout.encoding != 'UTF-8':
    sys.stdout = codecs.getwriter('UTF-8')(sys.stdout.buffer, 'strict')

# Define the possible moves
moves = ["rock", "paper", "scissors"]

play_again = 'y'
while play_again.lower() == 'y':
    # Prompt the user to enter their move
    print("Enter your move (rock, paper, or scissors):")
    player_move = input("\033[1mEnter your move (\U0001F5FF, \U0001F4C4, or \U0001F9FB):\033[0m ")

    # Generate a random move for the computer
    computer_move = random.choice(moves)

    # Determine the winner
    if player_move == computer_move:
        print("\033[93mIt's a tie!\033[0m")
    elif player_move == "rock" and computer_move == "scissors":
        print("\033[92mYou win!\033[0m")
    elif player_move == "paper" and computer_move == "rock":
        print("\033[92mYou win!\033[0m")
    elif player_move == "scissors" and computer_move == "paper":
        print("\033[92mYou win!\033[0m")
    else:
        print("\033[91mThe computer wins!\033[0m")

    # Print the computer's move
    print("\033[1mThe computer played " + computer_move + ".\033[0m")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (y/n) ")

