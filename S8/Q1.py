def count_case_characters(input_string):
    # Initialize counters for uppercase and lowercase
    uppercase_count = 0
    lowercase_count = 0
    
    # Iterate through each character in the string
    for char in input_string:
        if char.isupper():  # Check if the character is uppercase
            uppercase_count += 1
        elif char.islower():  # Check if the character is lowercase
            lowercase_count += 1
    
    # Print the results
    print(f"Number of uppercase characters: {uppercase_count}")
    print(f"Number of lowercase characters: {lowercase_count}")

# Example usage
input_string = input("Enter a string: ")
count_case_characters(input_string)
