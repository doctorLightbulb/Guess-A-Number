from random import randint


def you_guessed_right():
    random_selector = randint(0, 3)
    if random_selector == 0:
        message = "You guessed right!"
    elif random_selector == 1:
        message = "Wonderful! You guessed it!"
    elif random_selector == 2:
        message = "Stupendous work!"
    elif random_selector == 3:
        message = "Great job! Keep going!"
    return message


def you_guessed_wrong():
    random_selector = randint(0, 3)
    if random_selector == 0:
        message = "No. Give it another try!"
    elif random_selector == 1:
        message = "Sorry, try again!"
    elif random_selector == 2:
        message = "Not quite. Try again!"
    elif random_selector == 3:
        message = "Once more, please."
    return message


def only_numbers_are_allowed():
    random_selector = randint(0, 3)
    if random_selector == 0:
        message = "Sorry, only numbers are allowed."
    elif random_selector == 1:
        message = "Maybe in the future letters will equate to numbers, but currently, I'm afraid only numbers are recognized."
    elif random_selector == 2:
        message = "That is not a number!"
    elif random_selector == 3:
        message = "?"
    return message


def already_picked():
    random_selector = randint(0, 3)
    if random_selector == 0:
        message = "You already picked that number."
    elif random_selector == 1:
        message = "That number is so worn out! Try another one!"
    elif random_selector == 2:
        message = "It appears that you already guessed that number. Please try a different number."
    elif random_selector == 3:
        message = f"Hmm... try a number other than {guess}."
    return message


def sorry_you_lost():
    random_selector = randint(0, 3)
    if random_selector == 0:
        message = "Sorry, you lost!"
    elif random_selector == 1:
        message = "We are so sorry, but you appear to have lost."
    elif random_selector == 2:
        message = "It is with deep regret we inform you that you have lost the game."
    elif random_selector == 3:
        message = "Hmm... you lost. We are sorry!"
    return message


def you_won():
    random_selector = randint(0, 3)
    if random_selector == 0:
        message = "Congratulations! You win!"
    elif random_selector == 1:
        message = "A big round of applause! You've won!"
    elif random_selector == 2:
        message = "With great joy, we proudly name you the winner of the game!"
    elif random_selector == 3:
        message = "You have won! Stupendous work!"
    return message
