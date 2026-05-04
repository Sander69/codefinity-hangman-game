HIDDEN_SYMBOL="_"
alphabet = "abcdefghijklmnopqrstuvwxyz"

def get_guessed_word(secret_word, guessed_letters):
    return "".join(
        [letter if letter in guessed_letters else HIDDEN_SYMBOL for letter in secret_word]
    )

def main():
    secret_word = choose_word_random()
    guessed_letters = []
    # Example call to build and display the masked word
    masked = get_guessed_word(secret_word, guessed_letters)
    remaining = "".join([char for char in alphabet if char not in guessed_letters])
    print("Word to guess:", masked)

