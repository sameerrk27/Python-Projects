print("Welcome to Simple Chatbot:")
print("Type 'bye' to exit.")


while True:
    user_input = str(input("You:").lower())
    if user_input == "hi":
        print("Bot : Hi! I am your friendly chatbot")
    elif user_input == "how are you":
        print("Bot : I am doing great! Thank you for asking")
    elif user_input == "explain about python":
        print("Bot : Popular programming language used for web development, data analysis and AI ")
    elif user_input == "tell me your name":
        print("Bot : My name is Ultron and I am created by Tony Stark(IRON MAN).")
    elif user_input == "bye":
        print("Bot : Goodbye! Have a nice day. ")
        break
    else:
        print("Bot : Sorry, I don't understand your message.")
