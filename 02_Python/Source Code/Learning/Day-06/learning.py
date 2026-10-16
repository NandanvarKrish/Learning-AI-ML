# student = {"name" : "Krish", "Marks" : 98, "Passed" : True}

# print(student["name"]) # Prints name

# print(student.get("grade", "N/A")) # Check whether grade is there or not. If grade is in the dict. it prints the grade otherwise it prints the another provided string for e.g. "N/A"

# student["Grade"] = "A"
# print(student["Grade"])

# student["Marks"] = 99 # Update the existing value
# print(student["Marks"])

# del student["Passed"]
# print(student.get("Passed", "Passed removed"))

# if "name" in student:
#     print("Name found")

# else:
#     print("Name not found")
    
# for key, val in student.items():
#     print(f"{key} : {val}")


# LISTS OF DICTIONARIES

# dataset = [{"name" : "Krish", "marks" : 98, "passed" : 1, "hours" : 9},
#            {"name" : "Shyam", "marks" : 90, "passed" : 1, "hours" : 6},
#            {"name" : "Shiva", "marks" : 45, "passed" : 0, "hours" : 2},
#            {"name" : "Dhiren","marks" : 69, "passed" : 1, "hours" : 5}]

# for row in dataset:
#     status = "✅ Pass" if row["passed"] == 1 else "❌ Fail"
#     print(f"{row['name']:8} | {row['hours']} hrs | {row['marks']} marks | {status}")

# passed = [r for r in dataset if r["passed"] == 1]

# print(f"\n {len(passed)} passed out of {len(dataset)}")


# avg = sum(r["marks"] for r in dataset) / len(dataset)

# print(f"Avg: {avg:.2f}")


# data = {"name" : ["Krish", "Shivam", "Shiva", "Arsh"], "stuyd_hrs" : [10, 9, 8, 7], "marks" : [90, 54, 45, 50], "passed" : [True, True, False, True]}


# for i in range(len(data["name"])):
#     print(data["name"][i], "-->", data["marks"][i])


# student = {"name" : "Krish", "roll" : 1001, "marks" : 90, "city" : "Surat", "attendence": 85}

# # print(f"{student}")

# # print(student.get("grade", "N/A"))
# student["grade"] = "A"

# student["marks"] = 92
# del student["city"]
# # print(f"{student}")


# for key, val in student.items():
#     print(f"{key} : {val}")



# dataset = [{"name" : "Krish", "marks" : 98, "passed" : 1, "hours" : 9},
#            {"name" : "Shyam", "marks" : 90, "passed" : 1, "hours" : 6},
#            {"name" : "Shiva", "marks" : 45, "passed" : 0, "hours" : 2},
#            {"name" : "Dhiren","marks" : 69, "passed" : 1, "hours" : 5}]

# print(f"Total students: {len(dataset)}")

# avg_marks = sum(r["marks"] for r in dataset) / len(dataset)

# print(f"Average: {avg_marks:.2f}")

# passed = [r["passed"] for r in dataset if r["passed"] == 1]

# print(f"Total students passed: {len(passed)}")


# phonebook = {"name" : "krish", "Phone" : 9877896559,
#              "name" : "shyam", "Phone" : 9876543211,
#              "name" : "shiva", "Phone" : 9898989898,
#              "name" : "dhiren", "Phone" : 8768765443,
#              "name" : "shivam", "Phone" : 7665547876}

phonebook = {"name" : ["krish", "shyam", "shiva", "dhiren", "shivam"], "phone_num" : [9877896559, 9876543211, 9898989898, 8768765443, 7665547876]}

data = input("Enter the name: ").lower()


for i in range(len(phonebook["name"])):
    if phonebook["name"][i] == data:
        print(f"{phonebook['name'][i]} --> {phonebook['phone_num'][i]}")

