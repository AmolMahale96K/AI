import random

def hangman():
    # List of words for the game
    words = ["python", "programming", "hangman", "algorithm", "computer"]
    word = random.choice(words)
    guessed_letters = set()
    attempts = 6  # Number of attempts allowed
    word_progress = ["_" for _ in word]

    print("Welcome to Hangman!")
    print("Guess the word:", " ".join(word_progress))

    while attempts > 0:
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for idx, letter in enumerate(word):
                if letter == guess:
                    word_progress[idx] = guess
            print("Good guess:", " ".join(word_progress))
        else:
            attempts -= 1
            print(f"Incorrect guess! Attempts left: {attempts}")

        # Check if the word is completely guessed
        if "_" not in word_progress:
            print("Congratulations! You've guessed the word:", word)
            return

    print("Sorry, you've run out of attempts. The word was:", word)

# Run the Hangman game
hangman()
