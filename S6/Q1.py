import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Ensure that required NLTK resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')

def remove_stopwords_from_file(file_path):
    """
    Function to remove stopwords from a passage in a given text file.
    
    :param file_path: Path to the text file
    :return: The processed text without stopwords
    """
    # Read the content of the file
    with open(file_path, 'r') as file:
        text = file.read()

    # Tokenize the text into words
    words = word_tokenize(text)

    # Get the list of stop words
    stop_words = set(stopwords.words('english'))

    # Remove stopwords
    filtered_words = [word for word in words if word.lower() not in stop_words and word.isalnum()]

    # Join the filtered words back into a string
    filtered_text = ' '.join(filtered_words)
    
    return filtered_text

# Example usage
file_path = 'example.txt'  # Replace with the path to your text file
filtered_text = remove_stopwords_from_file(file_path)

print("Text without stopwords:")
print(filtered_text)
