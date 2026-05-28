import random
from player import Player
from extra_functions import is_even, is_greater, is_less


class GuessGame:
    def __init__(self):
        self.number = random.randint(1, 99)
        self.player = Player()
        self.is_running = True

    def start(self):
        print("The game is started")

        while self.is_running:
            user_input = input("Guess the number: ")

            self.process_input(user_input)

    def process_input(self, user_input):

        if user_input.lower() == "exit":
            print("Game ended")
            self.is_running = False
            return

        if user_input.lower() == "is the number even":
            self.show_hint()
            return

        if not user_input.isdigit():
            print("Please enter a valid number")
            return

        guessed_number = int(user_input)

        if guessed_number == self.number:
            print("You won!")
            print(f"Your score: {self.player.get_score()}")
            self.is_running = False
        else:
            print("Wrong guess")

            if is_greater(self.number, guessed_number):
                print("The secret number is GREATER")

            if is_less(self.number, guessed_number): 
                print("The secret number is LESS")

            self.player.decrease_score()

            if self.player.get_score() <= 0:
                print("No score left. Game over.")
                print(f"The number was {self.number}")
                self.is_running = False

    def show_hint(self):
        if is_even(self.number):
            print("The number is even")
        else:
            print("The number is odd")