# NLP --> Natural Language Processing

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# city = input("Enter your city: ")

# print(f"I am {name} from {city} and I'm {age} Y/O")

# favColor = input("Enter your fav color: ")
# print(f"Hey {name}, I'm glad that your favourite color is {favColor}")

# text = " Hello, World "

# print(text.strip())
# print(text.strip().upper())
# print(text.strip().lower())
# print(text.strip().replace("World", "AI"))
# print(text.strip().split(", "))

# sentence = "Python is great for Ai and ML"
# print(sentence.split(" "))


# NAME CARD GENERATOR

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# jobTitle = input("Enter your job title: ")
# hobby = input("Enter your hobby: ")

# print("="*35)
# print(f"Name      : {name}")
# print(f"Age       : {age}")
# print(f"Hobby     : {hobby}")
# print(f"Job Title : {jobTitle}")
# print("="*35)

# SPAM EMAIL CHECKER

# spamEmailText = input("Paste your email text here: ")

# print("free" in spamEmailText.lower())

# SASTA CLACULATOR

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# print("sum = ", num1+num2)
# print("difference = ", num1-num2)
# print("multiplicaton = ", num1*num2)
# print("division = ", num1/num2)
# print("modulus = ", num1%num2)

# FOR LOOP PREVIEW

# for i in range(5):
#     print("Hello, World!")

# NLP Text Cleaner — 3 bugs hidden below 
raw_text = " The Quick Brown Fox Jumps Over The Lazy Dog! " 
# Bug 1: wrong method name 
cleaned = raw_text.strip() 
# Bug 2: should be lowercase, not uppercase 
lower_text = cleaned.lower() 
# Bug 3: missing f prefix on f-string 
print(f"Word count: {len(lower_text.split())}")
