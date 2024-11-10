import random
import re

# Define a list of responses for each type of user input
responses = {
    "greeting": ["Hello! How can I help you today?", "Hi there! What can I do for you?", "Hello! How's it going?"],
    "goodbye": ["Goodbye! Have a great day!", "Bye! Take care!", "Goodbye, hope to chat again soon!"],
    "name": ["I am your friendly chatbot!", "You can call me Chatbot!", "I don't have a name, but you can call me whatever you like!"],
    "help": ["I'm here to assist you. You can ask me anything!", "How can I assist you today?", "What can I help you with?"],
    "default": ["Sorry, I didn't understand that.", "Could you please rephrase?", "I'm not sure what you mean."]
}

# Simple rules for pattern matching
def respond_to_input(user_input):
    user_input = user_input.lower()
    
    # Greeting
    if re.search(r'\b(hi|hello|hey|greetings)\b', user_input):
        return random.choice(responses["greeting"])
    
    # Goodbye
    elif re.search(r'\b(bye|goodbye|see you)\b', user_input):
        return random.choice(responses["goodbye"])
    
    # Asking for name
    elif re.search(r'\b(name|your name)\b', user_input):
        return random.choice(responses["name"])
    
    # Help
    elif re.search(r'\b(help|assist)\b', user_input):
        return random.choice(responses["help"])
    
    # Default response for unknown input
    else:
        return random.choice(responses["default"])

# Main chatbot loop
def chat():
    print("Chatbot: Hello! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if 'bye' in user_input.lower():
            print("Chatbot:", respond_to_input(user_input))
            break
        else:
            print("Chatbot:", respond_to_input(user_input))

# Start the chatbot
if __name__ == "__main__":
    chat()
