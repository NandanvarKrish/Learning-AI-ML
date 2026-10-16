# student = {"name" : "Krish", "roll" : 1001, "marks" : 90, "city" : "Surat", "attendence": 85}

# # print(f"{student}")

# # print(student.get("grade", "N/A"))
# student["grade"] = "A"

# student["marks"] = 92
# del student["city"]
# # print(f"{student}")


# for key, val in student.items():
#     print(f"{key} : {val}")

# print(student.get("email", "Not Found!"))



# dataset = [{"name" : "Krish", "marks" : 98, "passed" : 1, "hours" : 9},
#            {"name" : "Shyam", "marks" : 90, "passed" : 1, "hours" : 6},
#            {"name" : "Shiva", "marks" : 45, "passed" : 0, "hours" : 2},
#            {"name" : "Dhiren","marks" : 69, "passed" : 1, "hours" : 5}]

# print(f"Total students :- {len(dataset)}")

# avgMarks = sum(r["marks"] for r in dataset) / len(dataset)

# print(f"Average Marks :- {avgMarks:.2f}")

# passed = [r["passed"] for r in dataset if r["passed"] == 1]

# print(f"Total Students passed :- {len(passed)}")


# for row in dataset:
#     status = "✅ Passed" if row["passed"] == 1 else "❌ Fail"
#     print(f"{row['name']:6} | {row['marks']} | {row['passed']} | {row['hours']}")




# phonebook = {"name" : ["krish", "shyam", "shiva", "dhiren", "shivam"], "phone_num" : [9877896559, 9876543211, 9898989898, 8768765443, 7665547876]}

# data = input("Enter the name: ").lower()

# for i in range(len(phonebook['name'])):
#     if phonebook["name"][i] == data:
#         print(f"{phonebook['name'][i]} --> {phonebook['phone_num'][i]}")
#     else:
#         print("Contact Not Found")
#         break


# label_map = {0:"cat", 1:"dog", 2:"bird"}
# predictions = [0, 2, 1, 0, 2]

# for pred in predictions:
#     print(label_map.get(pred, "❌ERROR"))


# dataset = {"name" : ["krish", "shivam", "dhirendra", "arya", "aryan"], "marks" : [99, 45, 54, 89, 33], "passed" : [1, 0, 1, 1, 0]}

# for row in range(len(dataset['name'])):
#     print(f"{dataset['name'][row]:10} | {dataset['marks'][row]} | {dataset['passed'][row]}")


# student = {"name":"Krish", "marks":88}
# print(student.get("email", "Email Not Found"))

# for k, v in student.items():
#     print(f"{k}: {v}")

# # for k,v in student.items():
# #     print(f"{k}: {v}")

# config = {"lr": 0.001, "epochs" : 100}
# print(config)



# ADVANCED TASKS

# Task 1: Create, Update, and Delete

# student = {
#     "name": "krish",
#     "roll": 101,
#     "marks": 85,
#     "attendance": 90,
#     "city": "surat"
# }


# student["grade"] = "A"
# del student["city"]

# student["marks"] = 92

# print(f"{student}")


# Task 2: Safe Access with .get() and "in"


# user_profile = {
#     "name": "Krish",
#     "age": 25,
#     "role": "Student"
# }

# if "email" in user_profile:
#     print("Email exists")
# else:
#     print("Email Missing")

# print(user_profile.get("city", "city not found"))


# Task 3: Iterate with .items()


# car = {
#     "brand": "BMW",
#     "model": "M4 Competition",
#     "year": 2026,
#     "color": "Black"
# }


# for key, val in car.items():
#     print(f"{key} --> {val}")



# Task 4: List of Dictionaries (Filtering & Math)

# dataset = [
#     {"name": "Krish", "hours": 5, "marks": 88, "passed": 1},
#     {"name": "Shivam", "hours": 2, "marks": 45, "passed": 0},
#     {"name": "Dhiren", "hours": 8, "marks": 91, "passed": 1},
#     {"name": "Arya", "hours": 1, "marks": 32, "passed": 0}
# ]

#  # Students Passed
# studentsPassed = [r["passed"] for r in dataset if r["passed"] == 1]

# print(f"{len(studentsPassed)} students are passed")

# # Avg Marks

# avgMarks = sum(r["marks"] for r in dataset) / len(dataset)

# print(f"Average marks : {avgMarks:.2f}")


# 
# Task 5: Dictionary of Lists (Pandas Preview)

# data = {
#     "names": ["Krish", "Shivam", "Dhiren"],
#     "scores": [85, 92, 78]
# }

# for i in range(len(data)):
#     print(f"Name :- {data['names'][i]}")
#     print(f"Score :- {data['scores'][i]}\n\n")



