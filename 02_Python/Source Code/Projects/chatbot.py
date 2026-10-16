# PurePy Chatbot Dataset (105 Entries)
chatbot_dataset = [
    # GREETINGS
    {"hello": "Hello! I'm PurePy Bot. How can I help you today?"},
    {"hi": "Hi there! Ready to chat about Python and AI?"},
    {"hey": "Hey! What's on your mind?"},
    {"good morning": "Good morning! Hope you're having a great day."},
    {"good afternoon": "Good afternoon! How can I assist you?"},
    {"good evening": "Good evening! Ready to learn some Python?"},
    {"how are you": "I'm just code, but I'm running perfectly! How are you?"},
    {"what is your name": "I am PurePy Bot, built with 8 days of Python fundamentals!"},
    {"who are you": "I'm an AI chatbot demonstrating pure Python concepts."},
    {"who made you": "I was created by Krish using only basic Python, no libraries!"},
    {"what can you do": "I can answer questions about Python, AI, and general knowledge."},
    {"help": "Try asking about 'python', 'lists', 'functions', or 'machine learning'."},
    {"thanks": "You're very welcome! Happy to help."},
    {"thank you": "Anytime! Let me know if you need anything else."},
    {"goodbye": "Goodbye! Feel free to return whenever you want to chat."},
    
    # BOT CAPABILITIES
    {"what language are you written in": "I am written in 100% pure Python!"},
    {"do you use machine learning": "Not really! I use keyword matching and set logic."},
    {"are you smart": "I'm as smart as my dataset. Ask me something I know!"},
    {"where do you live": "I live in your computer's memory, running in Python."},
    {"what is your purpose": "To help you practice Python and answer questions!"},
    {"can you learn": "Not dynamically. Add new questions to my dataset to teach me."},
    {"how do you work": "I break your sentence into words and find the best match."},
    
    # PYTHON BASICS (Day 1-6)
    {"what is python": "Python is a high-level, readable programming language."},
    {"why python": "It's the #1 language for AI due to simplicity and libraries."},
    {"is python hard": "Not at all! It's logical and beginner-friendly."},
    {"what is a variable": "A named box that stores data, like `name = 'Krish'`."},
    {"what are data types": "str, int, float, and bool are the 4 basic types."},
    {"what is a string": "Text enclosed in quotes, like 'hello'."},
    {"how to get user input": "Use `input('Prompt: ')`. It always returns a string."},
    {"what is an f-string": "Embed variables in text: `f'Hello {name}'`."},
    {"what is a list": "Ordered, mutable collection: `[1, 2, 3]`."},
    {"what is a tuple": "Ordered, IMMUTABLE collection: `(1, 2, 3)`."},
    {"what is a set": "Unordered collection of UNIQUE items: `{1, 2, 3}`."},
    {"what is a dictionary": "Key-value pairs: `{'name': 'Ali', 'age': 20}`."},
    {"how to add to a list": "Use `.append()`: `my_list.append(5)`."},
    {"what is a for loop": "Iterates over sequences: `for x in list:`."},
    {"what is a while loop": "Repeats while condition is True."},
    {"what does break do": "Immediately exits the current loop."},
    {"what does continue do": "Skips to the next loop iteration."},
    {"what is a function": "Reusable code block defined with `def`."},
    {"what does return do": "Sends a value back to the caller."},
    {"what is list comprehension": "Create lists in one line: `[x**2 for x in range(5)]`."},
    
    # ADVANCED PYTHON (Day 7-8)
    {"what are *args": "Collects positional arguments into a tuple."},
    {"what are **kwargs": "Collects keyword arguments into a dictionary."},
    {"what is a lambda": "Anonymous one-line function: `lambda x: x*2`."},
    {"what does map do": "Applies a function to every item in a list."},
    {"what does filter do": "Keeps items where function returns True."},
    {"how to sort a list": "Use `.sort()` or `sorted(list, key=...)`."},
    {"what is indexing": "Access items by position: `my_list[0]`."},
    {"what is slicing": "Extract portion: `my_list[1:4]`."},
    {"how to check type": "Use `type(variable)`."},
    {"how to convert to string": "Use `str(25)`."},
    {"how to convert to int": "Use `int('25')`."},
    {"how to convert to float": "Use `float('3.14')`."},
    {"what is a boolean": "Data type that is True or False."},
    {"what is none": "Represents absence of a value."},
    {"how to comment in python": "Use `#` for single-line comments."},
    
    # AI & MACHINE LEARNING
    {"what is ai": "Simulation of human intelligence by machines."},
    {"what is machine learning": "Systems learn from data without explicit programming."},
    {"what is a dataset": "Collection of data used to train models."},
    {"what is a model": "Mathematical representation of learned patterns."},
    {"what is training": "Feeding data to an algorithm to learn patterns."},
    {"what is a neural network": "Brain-inspired computing system for deep learning."},
    {"what is deep learning": "Multi-layered neural networks for complex tasks."},
    {"what is nlp": "AI branch focused on human-computer language."},
    {"what is computer vision": "AI field enabling computers to understand images."},
    {"what is overfitting": "Model memorizes training data, fails on new data."},
    {"what is underfitting": "Model is too simple to capture patterns."},
    {"what is a feature": "Measurable property used for prediction."},
    {"what is a label": "The target outcome the model predicts."},
    {"what is supervised learning": "Learning from labeled data."},
    {"what is unsupervised learning": "Finding patterns in unlabeled data."},
    {"what is reinforcement learning": "Learning through rewards and punishments."},
    {"what is pandas": "Python library for data manipulation."},
    {"what is numpy": "Library for numerical computing and arrays."},
    {"what is scikit-learn": "Library for classical ML algorithms."},
    {"what is an epoch": "One full pass of training data."},
    
    # GENERAL KNOWLEDGE
    {"what is the capital of france": "The capital of France is Paris."},
    {"what is the largest planet": "Jupiter is the largest planet."},
    {"how many days in a year": "365 days, or 366 in a leap year."},
    {"how many days in a week": "There are 7 days in a week."},
    {"what is the speed of light": "Approximately 299,792 km per second."},
    {"who invented python": "Guido van Rossum, released in 1991."},
    {"what is the boiling point of water": "100°C or 212°F."},
    {"what is 2 plus 2": "4. I can do basic math!"},
    {"what is the square root of 144": "12."},
    {"what is the chemical symbol for water": "H2O."},
    {"who painted the mona lisa": "Leonardo da Vinci."},
    {"what is the largest ocean": "The Pacific Ocean."},
    {"how many continents are there": "7 continents on Earth."},
    {"what is the currency of japan": "The Yen."},
    {"what is the tallest mountain": "Mount Everest."},
    
    # FUN & FALLBACKS
    {"tell me a joke": "Why do programmers prefer dark mode? Light attracts bugs!"},
    {"another joke": "How many programmers to change a light bulb? None, that's hardware."},
    {"what is your favorite color": "I don't see color, but #00FF00 is popular."},
    {"do you like music": "I appreciate the math patterns in it!"},
    {"what is the meaning of life": "42, according to Douglas Adams."},
    {"can you sing": "Beep boop. Working on vocal synthesis!"},
    {"who is krish": "The awesome developer who built me!"},
    {"what is my name": "I don't know yet, but your dev is Krish!"},
    {"are you human": "No, I'm a Python script."},
    {"do you sleep": "I'm always awake and ready!"},
    {"quit": "Shutting down. Have a great day!"},
    {"exit": "Exiting chat. Happy coding!"},
    {"stop": "Stopping chatbot. Bye!"},
    {"i don't understand": "Could you rephrase that or type 'help'?"}
]


exiting = ["quit", "exit", "stop"]

def chatbot():
    while True:
        userText = input("You : ").lower().strip()

        if userText in exiting:
            print("NXKrish: Goodbye! Keep coding!")
            break


        for i in chatbot_dataset:
            for que, ans in i.items():
                if userText == que:
                    print(f"NXKrish: {ans}")

chatbot()