# age = int(input("Enter your age: "))
# marks = int(input("Enter your marks: "))

# if marks >= 90:
#     print("Grade: A")
# elif marks >= 70:
#     print("Grade: B")
# elif marks >= 50:
#     print("Grade: C")
# else:
#     print("❌ FAIL")

# if marks >= 50 and age >= 18:
#     print("Eligible for scholarship ✅")
# else:
#     print("Not eligible for scholarship ❌")

# if not marks < 50:
#     print("Pass ✅")
# else:
#     print("Fail ❌")

income = int(input("Monthly income (INR): ")) 
credit_score = int(input("Credit score (300-850): ")) 
age = int(input("Age: ")) 
if age >= 21 and income >= 50000 and credit_score >= 650:
    print("✅ Loan APPROVED") 
elif credit_score >= 600 and income >= 40000:
    print("⚠️ Conditionally approved — needs guarantor") 
else:
    print("❌ Loan REJECTED")
