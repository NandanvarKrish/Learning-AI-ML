# dataset = ["krish,95", "shivam,80", "arya,70", "dhiren,58"]

# with open("scores.txt","w") as f:
#     for i in range(len(dataset)):
#         f.write(dataset[i] + "\n")

# with open("scores.txt","r") as f:
#     context = f.read()

# print(context)

# with open("scores.txt", "a") as f:
#     f.write("\nSatyam,50")

# with open("scores.txt","r") as f:
#     context = f.read()

# # print(context)

# with open("scores.txt","r") as f:
#     for line in f:
#         name, score = line.strip().split(",")
#         print("-"*15)
#         print(f"|{name:6} | {score:3}|")
#         print("-"*15)

import csv
import os

script_dir = os.path.dirname(__file__)

students = [["name", "marks", "grade"], ["Krish", 95, "A+"], ["Dhiren", 80, "A"], ["shivam", 70, "B"]]

with open(os.path.join(script_dir, "students.csv"), "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(students)

with open(os.path.join(script_dir, "students.csv")) as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(f"{row['name']}: {row['marks']} ({row['grade']})")


data = [ {"name":"Ankit", "marks":49, "grade":"F"} ]

with open(os.path.join(script_dir, "new_student.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["name","marks","grade"])
    w.writeheader()
    w.writerows(data)

with open(os.path.join(script_dir, "new_student.csv")) as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(f"{row['name']}: {row['marks']} ({row['grade']})")


# import json

# config = { "model" : "RandomForest", "n_estimators" : 100, "max_depth" : 5, "accuracy" : 94.7, "features" : ["age", "income", "score"] }

# with open("config.json", "w") as f:
#     json.dump(config, f, indent=4)

# with open("config.json") as f:
#     loaded = json.load(f)
#     print(f"Model: {loaded['model']}")
#     print(f"n_estimators: {loaded['n_estimators']}")
#     print(f"Max Depth: {loaded['max_depth']}")
#     print(f"Accuracy: {loaded['accuracy']}")
#     print(f"Features: {loaded['features']}")

# json_str = json.dumps(config)
# # print(json_str)
# print(type(json_str))

# back = json.loads(json_str)
# # print(back)
# print(type(back))

# import csv, json, os
# def load_dataset(filepath):
#     """Load CSV and return list of dicts."""
#     if not os.path.exists(filepath):
#         print(f"File not found: {filepath}")
#         return []

#     with open(filepath) as f:
#         return list(csv.DictReader(f))

# def save_results(results, filepath): 
#     """Save prediction results to JSON."""
#     with open(filepath, "w") as f:
#         json.dump(results, f, indent=4)
            
#     print(f"Saved {len(results)} results to {filepath}") 
#     # Load → process → save pipeline
#     data = load_dataset("students.csv")
#     results = []
#     for row in data:
#         marks = int(row["marks"])
#         status = "pass" if marks >= 50 else "fail"
#         results.append({ "name" : row["name"], "marks" : marks, "status": status })
#         save_results(results, "results.json")
#         print(f"Processed {len(results)} students")
