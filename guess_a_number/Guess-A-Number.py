# Guess-A-Number
# version 1.0

from datetime import date, datetime
from random import randint

from random_messages import (
    already_picked,
    only_numbers_are_allowed,
    sorry_you_lost,
    you_guessed_right,
    you_guessed_wrong,
    you_won,
)

guess_count = 0
guess_limit = 3
round_count = 0
right_guesses = 0
wrong_guesses = 0
difficulty = 0
number = 10
command = ""
random_secret_numbers = []
guesses = []
introduction_message = "Welcome to Guess-A-Number!"
message = f"Guess a number between 1 and {number}"


def current_day():
    today = date.today()
    return today


def current_time():
    today = datetime.time(datetime.now())
    return today


catch_loop = True
message = introduction_message
print(message)

player_name = input("What would you like to be called? ")

while catch_loop:
    try:
        round_limit_choice = int(
            input("Select the number of rounds you would like to play: ")
        )
        catch_loop = False
    except ValueError:
        print(only_numbers_are_allowed())


catch_loop = True
while catch_loop:
    try:
        print(
            """
|=========================================================|
| 1. Beginner         2. Intermediate         3. Advanced |
| 4. Expert           5. Pro                  6. Pro++    |
|_________________________________________________________|
            """
        )
        difficulty = int(
            input("What difficulty level would you like to play? "),
        )
        catch_loop = False
    except ValueError:
        print(only_numbers_are_allowed())


if difficulty == 1:
    difficulty_name = "Beginner"
    maximum_number = 10
elif difficulty == 2:
    difficulty_name = "Intermediate"
    maximum_number = 25
elif difficulty == 3:
    difficulty_name = "Advanced"
    maximum_number = 40
elif difficulty == 4:
    difficulty_name = "Expert"
    maximum_number = 80
elif difficulty == 5:
    difficulty_name = "Pro"
    maximum_number = 100
elif difficulty == 6:
    difficulty_name = "Pro++"
    maximum_number = 1000


def random_numbers(input, maximum):
    for number in range(0, input):
        random_secret_numbers.append(randint(1, maximum))
    return random_secret_numbers


def calc_high_score(input, tries):
    rounds = 0
    for index in range(0, len(random_secret_numbers)):
        random_secret_numbers[index]
        rounds += 1
    if round_count != 0:
        score = right_guesses // input * 100
    else:
        score = 0
    return score


random_numbers(round_limit_choice, maximum_number)
message = f"Guess a number between 1 and {maximum_number}"
# Applications loop
while command != "0":
    if command == "1":
        # Restart the game.
        command = 0
        round_count = 0
        right_guesses = 0
        wrong = 0
        message = "Guess a number between 1 and 10"
        random_secret_numbers.clear()
        round_limit_choice = int(
            input("Select the number of rounds you would like to play: ")
        )
        random_numbers(round_limit_choice)
    # Game loop
    while round_count < round_limit_choice:
        print(message)
        # print(random_secret_numbers)
        catch_loop = True
        while catch_loop:
            try:
                guess = int(input("Guess: "))
                catch_loop = False
            except ValueError:
                print(only_numbers_are_allowed())
        catch_loop = True
        while catch_loop:
            if guess in guesses:
                message = already_picked()
                print(message)
                guess = int(input("Guess: "))
            else:
                catch_loop = False
        if guess == random_secret_numbers[round_count]:
            message = you_guessed_right()
            round_count += 1
            right_guesses += 1
            guess_count = 0
            guesses.clear()
        elif guess_count >= guess_limit:
            message = sorry_you_lost()
            break
        else:
            message = you_guessed_wrong()
            guess_count += 1
            wrong_guesses += 1
            guesses.append(guess)
    else:
        message = you_won()

    high_score = f"""

********************************************************************
*******                    YOUR HIGH SCORE                   *******
********************************************************************
{player_name}:
Difficulty: {difficulty_name}
Date: {current_day()}    Time: {current_time()}
Incorrect Guesses: {wrong_guesses}    Correct Guesses: {round_count}
Total Score: {calc_high_score(round_count, wrong_guesses)}%
            """
    print(message + high_score)
    catch_loop = True
    while catch_loop:
        command = input('Please press "1" to play again or "0" to exit: ')
        if command == "1" or command == "0":
            catch_loop = False
        else:
            print("Sorry, I do not understand.")

else:
    message = "You have successfully exited the game."
print(message)
