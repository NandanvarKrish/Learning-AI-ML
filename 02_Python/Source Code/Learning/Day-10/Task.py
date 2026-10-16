# f = open("scores.txt", "r")
# content = f.read()
# print(content)
# f.close()

# with open("scores.txt", "r") as f:
#     content = f.read()
#     print(content)

# import csv

# with open("students.csv", "r", newline="") as f:
#     reader = csv.DictReader(f)
#     data = list(reader)

#     for row in data:
#         print(row["name"], row["marks"], row["grade"])

# with open("results.csv", "w", newline="") as f:
#     writer = csv.DictWriter(f, fieldnames=["name", "grade"])
#     writer.writeheader()
#     writer.writerows({"name" : "Mayank", "grade" : "A"})

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

# dumps = json.dumps(config)
# print(dumps)

# dataset = ["krish,95", "shivam,80", "arya,70", "dhiren,58"]

# with open("scores.txt","w") as f:
#     for i in range(len(dataset)):
#         f.write(dataset[i] + "\n")

# with open("scores.txt","r") as f:
#     context = f.read()

# print(context)

# import csv

# with open("students.csv") as f:
#     reader = csv.DictReader(f)

#     for row in reader:
#         print(f"{row['name']}: {row['marks']} ({row['grade']})")

# import json

# config = { "model" : "RandomForest", "n_estimators" : 100, "max_depth" : 5, "accuracy" : 94.7, "features" : ["age", "income", "score"], "epoch": 100}

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

# import csv, json

# dataset = [10, 20, 30, 40, 50] # 5 data points
# weight = 1.0
# lr = 0.01 # learning rate
# # ep = []

# for epoch in range(3):
#         for data_point in dataset:
#             prediction = weight * data_point
#             error = prediction - 100
#             weight -= lr * error

#             # print(f"Epoch {epoch+1}, {weight:.4f}")

#             # ep.append({"epoch" : epoch,"weight" : weight})

#             with open("training_log.csv", "a", newline="") as f:
#                 f.write(f"Epoch: {epoch}, Weight: {weight:.4f}\n")

import json, csv, io

def get_grade(marks):
    if marks >= 80:
        return "A Grade"
    elif marks >= 60:
        return "B Grade"
    elif marks >= 50:
        return "C Grade"
    else:
        return "F Grade"

csv_data = '''name,marks
krish,95
shivam,80
arya,70
dhiren,58
Satyam,50
aryan,35
'''

reader = csv.DictReader(io.StringIO(csv_data))     
students = list(reader)
# print(students)

print("===Student Report===")
marks_list = []

for student in students:
    m = int(student['marks'])
    marks_list.append(m)
    grade = get_grade(m)
    status = "✅ Pass" if m >= 50 else "❌ Fail"

    print(f"{student['name']:6} | {m} | {grade} | {status}")

passed = [m for m in marks_list if m >= 50]
average = sum(marks_list) / len(marks_list)

print("=== Summary Stats ===")
print(f"Total Students: {len(students)} | Total Passed: {len(passed)} | Average: {average:.2f}")

model_config = {'total' : len(students), 'passed' : len(passed), 'average' : round(average,2)}

print(f"✅ Config saved to model_config.json")
print(f'JSON: {json.dumps(model_config, indent=2)}')

# To create new json file use 'with open()' function
