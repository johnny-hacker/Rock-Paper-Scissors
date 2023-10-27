class RPSGame:

    def __init__(self, user, computer):
        self.user_choice = user
        self.computer_choice = computer
        self.rock = "rock"
        self.paper = "paper"
        self.scissors = "scissors"
    
    def game(self):
        # Compare/decide the winner and display
        # if user selected rock
        if self.user_choice == self.rock:
            # and the computer selected rock, it's a tie
            if self.computer_choice == self.rock:
                print("It's a tie, try again!!!\n")
                pass
            # and the computer selected paper, the computer wins
            elif self.computer_choice == self.paper:
                print("Computer wins!!!\n")
            # and the computer selected scissors, the user wins
            else:
                print("User wins!!!\n")

        # if user selected paper
        elif self.user_choice == self.paper:

            # and the computer selected rock, the user wins
            if self.computer_choice == self.rock:
                print("User wins!!!\n")

            # and the computer selected paper, it's a tie
            elif self.computer_choice == self.paper:
                print("It's a tie, try again!!!\n")
                pass
            # and the computer selected scissors, the computer wins
            else:
                print("Computer wins!!!\n")

        # if user selected scissors
        elif self.user_choice == self.scissors:
            # and the computer selected rock, computer wins
            if self.computer_choice == self.rock:
                print("Computer wins!!!\n")

            # and the computer selected paper, user wins
            elif self.computer_choice == self.paper:
                print("User wins!!!\n")

            # and the computer selected scissors, it's a tie
            else:
                print("It's a tie, try again!!!\n")
