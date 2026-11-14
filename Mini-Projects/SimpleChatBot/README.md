# Simple ChatBot

A beginner-friendly Python project that simulates a simple chatbot. It interacts with the user by responding to predefined messages and keeps running until the user types `bye`.

## What This Program Does
This program:
- takes input from the user
- checks the input using conditions
- replies with predefined answers
- keeps running in a loop until the user exits

It is a great beginner project to learn how to build simple interactive programs.

## Key Concepts Used
1. `while` loop
2. `if-elif-else` conditions
3. `input()` and `print()` functions
4. String methods like `lower()`

## Project Idea
The chatbot asks the user for input and responds based on what was typed. For example:
- if the user says `hi`, the bot greets them
- if the user says `hello`, the bot responds politely
- if the user says `bye`, the bot exits

## Python Code
```python
print("Welcome to Simple Chatbot!")
print("Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hi":
        print("Bot: Hi! I am your friendly chatbot.")
    elif user_input == "hello":
        print("Bot: Hello! How can I help you?")
    elif user_input == "how are you":
        print("Bot: I'm doing great, thank you!")
    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break
    else:
        print("Bot: Sorry, I didn't understand that.")
```

## Sample Output
```text
Welcome to Simple Chatbot!
Type 'bye' to exit.

You: hi
Bot: Hi! I am your friendly chatbot.

You: bye
Bot: Goodbye! Have a nice day.
```

## Screen Recording / Demo Output
You can attach a short screen recording or a screenshot of the program running in the terminal.

Example placeholder:

```text
[Add your screen recording or demo GIF here]
```

## How to Run
1. Save the file as `simplechatbot.py`
2. Open your terminal or command prompt
3. Run the program using:

```bash
python simplechatbot.py
```

## Conclusion
This project is a simple and effective way to learn:
- loops
- conditional statements
- user input handling
- basic text processing

It is a perfect beginner project for anyone starting with Python programming.
