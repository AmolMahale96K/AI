import random

# List of words to choose from
words = ['python', 'java', 'hangman', 'programming', 'developer', 'computer']

# Function to display the current state of the word with blanks
def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

# Function to play the Hangman game
def play_hangman():
    # Choose a random word from the list
    word = random.choice(words)
    guessed_letters = set()
    wrong_guesses = set()
    attempts_left = 6  # Number of wrong attempts allowed
    
    print("Welcome to Hangman!")
    print("You have 6 attempts to guess the word.")
    
    while attempts_left > 0:
        print(f"\nCurrent word: {display_word(word, guessed_letters)}")
        print(f"Wrong guesses: {', '.join(wrong_guesses)}")
        print(f"Attempts left: {attempts_left}")
        
        # Get user input (single letter guess)
        guess = input("Enter a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        # If the letter was guessed before, prompt the user
        if guess in guessed_letters or guess in wrong_guesses:
            print("You already guessed that letter.")
            continue
        
        # Check if the guess is correct
        if guess in word:
            guessed_letters.add(guess)
            print(f"Good guess! {guess} is in the word.")
        else:
            wrong_guesses.add(guess)
            attempts_left -= 1
            print(f"Wrong guess! {guess} is not in the word.")
        
        # Check if the player has guessed all the letters
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You guessed the word: {word}")
            break

    # If the player runs out of attempts
    if attempts_left == 0:
        print(f"\nGame over! The word was: {word}")

# Run the Hangman game
play_hangman()
