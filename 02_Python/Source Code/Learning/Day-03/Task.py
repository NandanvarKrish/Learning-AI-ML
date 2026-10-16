# STUDENT GRADE ACCORDING TO MARKS

# marks = int(input("Enter your marks: "))
# attendence = int(input("Enter your age (%): "))

# if marks >= 90:
#     print("Grade: A")
# elif marks >= 70:
#     print("Grade: B")
# elif marks >= 50:
#     print("Grade: C")
# else:
#     print("❌ FAIL")

# STUDENT PASS/FAIL ACCORDING TO MARKS AND ATTENDENCE

# if marks >= 50 and attendence >= 75:
#     print("Pass ✅")
# else: 
#     print("Fail ❌")

# BANK LOAN APPROVAL

# income = int(input("Monthly income (INR): ")) 
# credit_score = int(input("Credit score (300-850): ")) 
# age = int(input("Age: ")) 
# if age >= 21 and income >= 50000 and credit_score >= 650:
#     print("✅ Loan APPROVED") 
# elif credit_score >= 600 and income >= 40000:
#     print("⚠️ Conditionally approved — needs guarantor") 
# else:
#     print("❌ Loan REJECTED")

# TEMPERATURE ADVISOR

# temp = int(input("Enter temperature (in C): "))

# if temp <= 0:
#     print("Freezing ❄️")
# elif temp <= 15:
#     print("Cold ❄️")
# elif temp <= 30:
#     print("Warm ♨️")
# else:
#     print("Hot 🥵")

# BMI CALCULATOR


# weight = int(input("Enter your weight (in Kg): "))
# height = int(input("Enter your height (in m): "))

# bmi = weight/(height ** 2)

# if bmi <= 18.5:
#     print("Under Weight")
# elif bmi <= 25:
#     print("Normal")
# elif bmi <= 35:
#     print("Over weight")
# else:
#     print("Obese")


# AI SPAM EMAIL CHECKER

# email = input("Enter email text: ").lower() # Day 02 + Day 03! 
# spam_words = ["free", "win", "click", "urgent", "congratulations", "prize"]
# found = [] 
# for word in spam_words: 
#     if word in email: 
#         found.append(word) 

#     if len(found) >= 2: 
#         print(f"🚨 HIGH SPAM — {len(found)} spam words: {found}")

#     elif len(found) == 1: 
#         print(f"⚠️ SUSPICIOUS — contains: {found}") 

#     else: print("✅ CLEAN — no spam words detected")


# FIND AND FIX THE BUGS

# weight = float(input("Weight (kg): "))
# height = float(input("Height (m): "))
# bmi = weight / height ** 2

# if bmi < 18.5:
#     print("Underweight")

# elif bmi < 25.0: 
#     print("Normal") 

# elif bmi < 30.0: 
#     print("Overweight")

# else:
#     print("Obese")

# marks = 75

# if marks >= 90:
#     print("A")

# if marks >= 70:
#     print("B")

# if marks >= 50:
#     print("C")

if False:
    print("One")
elif True:
    print("Two")
else:
    print("Three")
