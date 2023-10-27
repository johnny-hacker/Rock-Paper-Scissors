class UserChoice:

    def __init__(self):
        self.rock = "rock"
        self.paper = "paper"
        self.scissors = "scissors"
        self.user_choice = ""
        self.choice()

    def choice(self):

        # get the users input
        user_input = input("Choose between rock, paper, or scissors: ")

        while user_input:

            # if the user chooses rock
            if user_input == self.rock:
                self.user_choice = self.rock
                user_input = False
            # if the user chooses paper
            elif user_input == self.paper:
                self.user_choice = self.paper
                user_input = False
            # if the user chooses scissors
            elif user_input == self.scissors:
                self.user_choice = self.scissors
                user_input = False
            else:
                print("Do didn't answer correctly, choose either")
                user_input = input("Choose between rock, paper, or scissors: ")

