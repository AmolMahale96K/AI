import string

def remove_punctuations(input_string):
    # Create a translation table to remove punctuations
    translator = str.maketrans('', '', string.punctuation)
    # Remove punctuation using translate method
    return input_string.translate(translator)

# Example usage
input_string = "Hello, world! This is an example string... with punctuations!!!"
output_string = remove_punctuations(input_string)
print("Original String: ", input_string)
print("String without Punctuation: ", output_string)
