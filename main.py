import random

# Function to generate a bot response
def get_bot_response(user_input):
    bot_responses = [
        "Hello!",
        "How are you?",
        "Nice to meet you!",
        "What can I do for you?",
        "Tell me more.",
        "That's interesting.",
        "I'm sorry, I don't understand.",
        "Could you please rephrase that?"
    ]
    return random.choice(bot_responses)

# Main loop
while True:
    user_input = input("User: ")
    bot_response = get_bot_response(user_input)
    print("Bot:", bot_response)