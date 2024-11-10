import string

def remove_punctuation(input_string):
    # Remove punctuation using a generator expression
    cleaned_string = ''.join(char for char in input_string if char not in string.punctuation)
    return cleaned_string

# Input string
input_string = input("Enter a string with punctuation: ")

# Remove punctuation and display result
result = remove_punctuation(input_string)
print("String without punctuation:", result)
