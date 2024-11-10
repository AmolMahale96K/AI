import itertools

# Function to solve the cryptarithmetic equation
def solve_cryptarithmetic():
    # All digits from 0 to 9
    digits = range(10)
    
    # List of unique letters in the cryptarithmetic equation
    letters = 'TWOFRU'
    
    # Create a list of all possible permutations of the digits for the letters
    for perm in itertools.permutations(digits, len(letters)):
        # Create a dictionary to map letters to digits
        letter_to_digit = dict(zip(letters, perm))
        
        # Get the digits for TWO, FOUR
        TWO = letter_to_digit['T'] * 100 + letter_to_digit['W'] * 10 + letter_to_digit['O']
        FOUR = letter_to_digit['F'] * 1000 + letter_to_digit['O'] * 100 + letter_to_digit['U'] * 10 + letter_to_digit['R']
        
        # Check if the equation TWO + TWO = FOUR holds
        if TWO + TWO == FOUR:
            # If the equation holds, print the result
            print(f"Solved: TWO + TWO = FOUR")
            print(f"T = {letter_to_digit['T']}, W = {letter_to_digit['W']}, O = {letter_to_digit['O']}, F = {letter_to_digit['F']}, U = {letter_to_digit['U']}, R = {letter_to_digit['R']}")
            print(f"TWO = {TWO}, FOUR = {FOUR}")
            return
    
    print("No solution found.")

# Call the function to solve the cryptarithmetic problem
solve_cryptarithmetic()
