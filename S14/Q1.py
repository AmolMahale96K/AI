def sort_sentence(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Sort the words alphabetically
    words.sort()
    
    # Join the sorted words back into a sentence
    sorted_sentence = ' '.join(words)
    
    return sorted_sentence

# Input sentence from the user
sentence = input("Enter a sentence: ")

# Sort the sentence
sorted_sentence = sort_sentence(sentence)

# Print the sorted sentence
print("Sorted sentence:", sorted_sentence)
