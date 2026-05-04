import random  # Importing the random module

# List of words used for the Hangman game
WORDS = [
    "python",
    "hangman",
    "developer",
    "console",
    "project",
    "function",
    "integer",
    "variable"
]

# Symbol used to represent hidden letters
HIDDEN_SYMBOL = "_"

# Maximum number of incorrect attempts allowed
MAX_ATTEMPTS = 6


def choose_word_random():
    # Returning a random word from the list
    return random.choice(WORDS)


def is_word_guessed(secret_word, guessed_letters):
    # Checking whether all letters of the word are guessed
    return all(letter in guessed_letters for letter in secret_word)


def get_guessed_word(secret_word, guessed_letters):
    # Creating a masked version of the secret word
    return "".join(
        [letter if letter in guessed_letters else HIDDEN_SYMBOL for letter in secret_word]
    )


def get_available_letters(guessed_letters):
    # Returning letters that have not been guessed yet
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return "".join([char for char in alphabet if char not in guessed_letters])


def hints_match(pattern, candidate):
    # Checking if the pattern and candidate match
    if len(pattern) != len(candidate):
        return False

    for i in range(len(pattern)):
        if pattern[i] != HIDDEN_SYMBOL and pattern[i] != candidate[i]:
            return False

    return True


def show_possible_matches(pattern):
    matched = []
    for word in WORDS:
        if hints_match(pattern, word):
            matched.append(word)
    return matched



def main():
    # Entry point for the game
    pass


if __name__ == "__main__":
    main()