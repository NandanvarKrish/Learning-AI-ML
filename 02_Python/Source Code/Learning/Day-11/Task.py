# def validate_marks(marks):
#     try:
#         m = float(marks)
import csv

#         if not (0 <= m <= 100):
#             raise ValueError(f"marks must be 0-100, got {m}")
#             grade = "A" if m>=80 else "B" if m>=60 else "F"
#             print(f"Marks :- {marks}, Grade :- {grade}")
    
#     except ValueError as e:
#         print(f"Value Error : {e}")

#     finally:
#         print("✅Validation is complete")

# for test in [90, 75, "abc", 150, -55]:
#     validate_marks(test)


# try:
#     n = float(input("Enter the number: "))
#     print(f"You entered {n}")
# except ValueError as e:
#     print(f"ValueError: {e}")

# finally:
#     print("✅ Program executed Successfully")

# try:
#     num = int(input("Enter numerator: "))
#     den = int(input("Enter denominator: "))
#     frac = num/den
#     print(frac)
# except ZeroDivisionError as e:
#     print(f"ZeroDivisionError: {e}")
# finally:
#     print("✅ Program executed Successfully")

# def validate_age(age):
#     if age < 0:
#         raise ValueError('Age cannot be negative')
#     else:
#         return age
# try:
#     age = int(input("Enter your age: "))
#     validate_age(age)
#
# except ValueError as e:
#     print(f"ValueError: {e}")
# finally:
#     print("Goodbye!")

# import csv
#
# def openfile(filepath):
#     with open(filepath, "r") as f:
#         reader = csv.DictReader(f)
#         # print(reader)
# try:
#     openfile("scores.csv")
# except FileNotFoundError as e:
#     print(F"File not found: {e}")
# finally:
#     print("Done")

# errors = []
# corrects = []
# data = [99, 105, "abc", 78, 7878, 45]
#
# for i,m in enumerate(data):
#     try:
#         m = float(m)
#         if not 0 <= m <= 100:
#             raise ValueError(f"Value {m} is out of range")
#         corrects.append(m)
#
#     except ValueError as e:
#         print(f"ValueError: {e}")
#         errors.append(m)
#
# print(f"Errors: {errors}")
# print(f"Corrects: {corrects}")

# students = {"name" : "Krish", "age" : 18, "sport" : "Volleyball"}
#
# try:
#     print(students["email"])
#
# except KeyError as e:
#     print(f"Missing Field: {e}")

try:
    data = [10, 20, 30]
    # result = data[5]
    val = 10/0

except IndexError:
    print("Index out of range")

except ZeroDivisionError:
    print("Cannot divide by zero")

except Exception as e:
    print(f"Unexpected: {e}")
