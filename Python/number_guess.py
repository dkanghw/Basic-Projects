import re
import math
import random


def input_filter(word):
    guess_pattern = re.compile(r"Guess", re.IGNORECASE)
    set_pattern = re.compile(r"Set", re.IGNORECASE)

    guess_matches = guess_pattern.findall(word)
    set_matches = set_pattern.findall(word)

    return guess_matches, set_matches


def guess_Function():

    attempt_count = 0
    random_value = random_Number()

    while (True):
        attempt_count += 1
        number_pick = int(
            input("Pick a number between 1 and 100 inclusive\n"))
        if (number_pick < random_value):
            print("Too low, Try again.\n")
        elif (number_pick > random_value):
            print("Too high, Try again.\n")
        else:
            print("Correct")
            break

    print("Attempted count: %i " % attempt_count)


def set_Function():
    print("Set")


def unknownWord_ErrorCatch():
    print("Unknown Word")


def random_Number():
    min_value = 1
    max_value = 100
    random_value = random.randint(min_value, max_value)

    return random_value


def main():
    input_word = input("Guess or Set?: \n")

    guess_matches, set_matches = input_filter(input_word)

    for match in guess_matches:
        guess_Function()

    for match in set_matches:
        set_Function()


if __name__ == "__main__":
    main()
