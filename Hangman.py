import random
import string

def get_random_word():
    # List of words for the Hangman game
    words = ['python', 'hangman', 'programming', 'challenge', 'code', 'smile']
    return random.choice(words)


def display_word(word, guessed_letters):
    # Display the word with guessed letters revealed
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)


def hangman_game():
    # Start the game
    word = get_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6  # Number of allowed incorrect guesses

    # Hangman stages
    hangman_stages = [
        """
          +---+
          |   |
          |   |
          |   |
         =======
        """,
        """
          +---+
          |   |
          |   O
          |   |
         =======
        """,
        """
          +---+
          |   |
          |   O
          |  / |
         =======
        """,
        """
          +---+
          |   |
          |   O
          |  /|\
         =======
        """,
        """
          +---+
          |   |
          |   O
          |  /|\
          |  /
         =======
        """,
        """
          +---+
          |   |
          |   O
          |  /|\
          |  / \
         =======
        """
    ]

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")

    while incorrect_guesses < max_incorrect_guesses:
        print("\n" + hangman_stages[incorrect_guesses])
        print(display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        if guess in word:
            guessed_letters.add(guess)
            print("Good guess!")
        else:
            incorrect_guesses += 1
            print(f"Incorrect guess! You have {max_incorrect_guesses - incorrect_guesses} tries left.")

        if set(word) == guessed_letters:
            print(f"\nCongratulations! You've guessed the word: {word}")
            break
    else:
        print(f"\nSorry, you've run out of tries. The word was: {word}")


if __name__ == "__main__":
    hangman_game()