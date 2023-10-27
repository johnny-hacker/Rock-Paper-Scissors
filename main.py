# Programmer: Olmedo, Johnny

# Submission date: 10/27/2023

# This program lets you play rock paper scissors with the computer, using Object-Oriented Programming

from UserChoice import UserChoice
from ComputerChoice import ComputerChoice
from RPSGame import RPSGame


def main():
    # call computer choice
    computer_choice = ComputerChoice().computer_choice

    # call user choice
    user_choice = UserChoice().user_choice

    # play the game
    RPSGame(user_choice, computer_choice).game()


main()
