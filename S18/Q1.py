import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download NLTK stopwords if not already downloaded
nltk.download('punkt')
nltk.download('stopwords')

def remove_stopwords(file_path):
    # Read the contents of the file
    with open(file_path, 'r') as file:
        text = file.read()

    # Tokenize the text into words
    words = word_tokenize(text)
    
    # Get the set of English stopwords from NLTK
    stop_words = set(stopwords.words('english'))

    # Remove stopwords from the text
    filtered_words = [word for word in words if word.lower() not in stop_words]

    # Join the filtered words back into a string
    cleaned_text = ' '.join(filtered_words)

    # Print and save the cleaned text
    print("Original Text:")
    print(text)
    print("\nCleaned Text (without stopwords):")
    print(cleaned_text)
    
    # Optionally, save the cleaned text to a new file
    with open('cleaned_text.txt', 'w') as output_file:
        output_file.write(cleaned_text)

# Provide the path to your text file
file_path = 'input.txt'  # Replace with your file path
remove_stopwords(file_path)
