import re


def input_filter(word):
    guess_pattern = re.compile(r"Guess", re.IGNORECASE)
    set_pattern = re.compile(r"Set", re.IGNORECASE)

    guess_matches = guess_pattern.findall(word)
    set_matches = set_pattern.findall(word)

    return guess_matches, set_matches


def guess_function():
    print("Guess")


def set_function():
    print("Set")


def unknownWord_ErrorCatch():
    print("Unknown Word")


def main():
    input_word = input("Guess or Set?: \n")

    guess_matches, set_matches = input_filter(input_word)

    for match in guess_matches:
        guess_function()

    for match in set_matches:
        set_function()

    if (not guess_matches or not set_matches):
        unknownWord_ErrorCatch()


if __name__ == "__main__":
    main()
