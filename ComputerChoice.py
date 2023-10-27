import random


class ComputerChoice:

    def __init__(self):
        self.rock = 1
        self.paper = 2
        self.scissors = 3
        self.computer_choice = 0
        self.choice()

    def choice(self):
        # Generate random number and store
        self.computer_choice = random.randint(1, 3)

        # Display computers choice
        # if the random number is 1 the choice is rock
        if self.computer_choice == self.rock:
            # set computer choice to the word "rock"
            self.computer_choice = "rock"
            print(f"Computer's choice is {self.computer_choice}\n")

        # if the random number is 2 the choice is paper
        elif self.computer_choice == self.paper:
            # set computer choice to the word "paper"
            self.computer_choice = "paper"
            print(f"Computer's choice is {self.computer_choice}\n")

        # if the random number is 3 the choice is scissors
        else:
            # set computer choice to the word "scissors"
            self.computer_choice = "scissors"
            print(f"Computer's choice is {self.computer_choice}\n")
