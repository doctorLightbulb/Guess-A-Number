"""A simple guessing game that employs regex to match user input and a machine
learning algorithm to process the computer's answers.

December 3, 2024
"""

__version__ = "0.0.1"

import os
import random
import re
from typing import Set

# User input can be a number, a string, or a list of numbers interspersed with
# letters or words.


class RandomNumber:
    """Generate a random number based on `level`, `min_number` and
    `max_number`."""

    def __init__(self) -> None:
        self.level = 1
        self.max_number = 10
        self.min_number = 1

    def reset_secret_number(self):
        return random.randint(
            self.min_number,
            self.max_number,
        )


class GuessingGame:
    def __init__(self, number_generator: RandomNumber) -> None:
        self.number_generator = number_generator
        self.numbers_pattern = re.compile(r"\d+")
        self.level = self.number_generator.level
        self.max_number = self.number_generator.max_number
        self.min_number = self.number_generator.min_number
        self.secret_number = self.number_generator.reset_secret_number()

        self.max_guesses = 3
        self.guesses: Set[int] = set()

    def play(self):
        self.guesses.clear()
        while len(self.guesses) < self.max_guesses:
            guess = input("Guess: ")
            guesses = self.numbers_pattern.findall(guess)
            guesses = [int(_) for _ in guesses]

            if not guesses:
                print("Please enter a number, not a letter or symbol.")
                continue

            for guess in guesses:
                has_won = self.evaluate_guess(guess)

                if guess in self.guesses:
                    print("You have already tried those numbers.")
                else:
                    self.guesses.add(guess)

                if has_won:
                    self.number_generator.reset_secret_number()
                    return self.guesses
        print(
            f"Sorry, the number was {self.secret_number};",
            "you lose.",
        )
        return self.guesses

    def evaluate_guess(self, guess: int):
        secret_number = self.secret_number
        max_guesses = self.max_guesses

        if guess == self.secret_number:
            print("You win!")
            return True
        elif guess < secret_number and len(self.guesses) != max_guesses:
            print("Too low. Try again!")
        elif guess > secret_number and len(self.guesses) != max_guesses:
            print("Too high. Try again!")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def app():
    number_generator = RandomNumber()
    game = GuessingGame(number_generator)

    clear_screen()
    print("Welcome to Guess-A-Number 2.0!")
    while True:
        try:
            print("Press any key to play a round!")
            input("")
            print(
                f"I am thinking of a number between {game.min_number}",
                f"and {game.max_number}.",
                "\nCan you guess what it is in less than three tries?\n",
            )
            game.play()
        except KeyboardInterrupt:
            clear_screen()
            print("Goodbye!")
            break


def main():
    app()


if __name__ == "__main__":
    main()
