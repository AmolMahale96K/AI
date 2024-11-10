import random
import time

def chatbot():
    # Predefined set of responses
    greetings = ['hi', 'hello', 'hey', 'hola']
    farewells = ['bye', 'goodbye', 'see you', 'later']
    responses = {
        'how are you': ["I'm good, thank you!", "I'm doing well, how about you?", "I'm great! How can I assist you today?"],
        'what is your name': ["I'm a chatbot created to assist you.", "I'm your friendly chatbot!", "You can call me Chatbot."],
        'what can you do': ["I can chat with you, answer basic questions, and provide assistance.", 
                            "I can help you with queries, play games, and much more.", "I can chat, give advice, and help you solve problems!"],
        'default': ["Sorry, I don't understand that.", "Could you clarify?", "I didn't get that. Can you ask something else?"]
    }

    print("Chatbot: Hi! I'm a simple chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input in farewells:
            print("Chatbot: Goodbye! Have a great day!")
            break

        elif user_input in greetings:
            print(f"Chatbot: {random.choice(['Hello!', 'Hi there!', 'Hey! How are you?'])}")

        elif user_input in responses:
            print(f"Chatbot: {random.choice(responses[user_input])}")

        else:
            print(f"Chatbot: {random.choice(responses['default'])}")

        # Simulate typing delay
        time.sleep(1)

# Run the chatbot
chatbot()
