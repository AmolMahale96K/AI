from itertools import permutations

def solve_cryptarithmetic():
    # Letters involved in the equation
    letters = 'TWOFRU'
    
    # Generate all possible digit assignments (0-9) for these 6 letters
    for perm in permutations(range(10), len(letters)):
        # Create a dictionary that maps letters to digits
        letter_to_digit = dict(zip(letters, perm))
        
        # Convert words into numbers based on the current digit mapping
        TWO = letter_to_digit['T'] * 100 + letter_to_digit['W'] * 10 + letter_to_digit['O']
        FOUR = letter_to_digit['F'] * 1000 + letter_to_digit['O'] * 100 + letter_to_digit['U'] * 10 + letter_to_digit['R'] 
        
        # Check if the equation TWO + TWO = FOUR holds true
        if TWO + TWO == FOUR:
            print(f"Solution found:")
            print(f"TWO = {TWO}, FOUR = {FOUR}")
            print(f"Mapping: T={letter_to_digit['T']}, W={letter_to_digit['W']}, O={letter_to_digit['O']}, "
                  f"F={letter_to_digit['F']}, U={letter_to_digit['U']}, R={letter_to_digit['R']}")
            return

    print("No solution found.")

# Run the cryptarithmetic solver
solve_cryptarithmetic()
