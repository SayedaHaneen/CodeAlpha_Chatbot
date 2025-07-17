def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    # Greetings
    if user_input in ["hello", "hi", "hey"]:
        return "Hi there! 😊"
    
    # How are you
    elif user_input in ["how are you", "how are you doing"]:
        return "I'm doing great, thanks for asking! How about you?"
    
    # Asking name
    elif user_input in ["what is your name", "your name?", "who are you"]:
        return "I'm ChatBot Alpha, your friendly helper!"
    
    # Capabilities
    elif user_input in ["what can you do", "help", "features"]:
        return "I can chat with you, respond to basic questions, and keep you company! 💬"
    
    # Thank you
    elif user_input in ["thank you", "thanks"]:
        return "You're welcome! 😊"
    
    # Exit
    elif user_input in ["bye", "goodbye", "exit"]:
        return "Goodbye! Have a nice day! 👋"
    
    # Default response
    else:
        return "Hmm... I don't understand that yet. Try something else!"

# Chatbot loop
print("=== Welcome to ChatBot Alpha ===")
print("Say 'bye' anytime to exit.\n")

while True:
    user_message = input("You: ")
    reply = chatbot_response(user_message)
    print("Bot:", reply)

    if user_message.lower().strip() in ["bye", "goodbye", "exit"]:
        break
