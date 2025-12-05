import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list WORDS."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the game state."""
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def get_valid_guess(guessed_letters):
    """Checks if the user input is a single letter and
    if the guessed letter is already in the list of guessed letters.
    Keeps prompting the user to enter a single letter until a valid guess was entered
    """
    while True:
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print(f"You already guessed the letter {guess}!\n")
        elif len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.\n")
        else:
            return guess


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1
    print("Welcome to Snowman Meltdown!")

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = get_valid_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            mistakes += 1
            print(f"Bad guess, '{guess}' is not in the word.")

        if mistakes >= max_mistakes:
            display_game_state(mistakes, secret_word, guessed_letters)
            print(f"Oh no, the snowman melted! The word was: {secret_word}")
            break

        if all(letter in guessed_letters for letter in secret_word):
            display_game_state(mistakes, secret_word, guessed_letters)
            print("Congratulations! You saved the snowman!")
            break