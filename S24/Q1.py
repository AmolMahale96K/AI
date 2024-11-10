def sort_sentence(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Sort the words in alphabetical order
    sorted_words = sorted(words)
    
    # Join the sorted words back into a sentence
    sorted_sentence = ' '.join(sorted_words)
    
    return sorted_sentence

# Example usage
sentence = "The quick brown fox jumps over the lazy dog"
sorted_sentence = sort_sentence(sentence)
print("Original Sentence: ", sentence)
print("Sorted Sentence: ", sorted_sentence)
