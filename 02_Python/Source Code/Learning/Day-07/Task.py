# def get_grade(marks):
#     if marks >= 80:
#         return "A Grade"
#     elif marks >= 60:
#         return "B Grade"
#     elif marks >= 50:
#         return "C Grade"
#     else:
#         return "F Grade"

# studentMarks = [88, 45, 72, 33, 91]

# grades = [get_grade(s) for s in studentMarks]

# print(grades)


# def bmi(weight, height, unit="metric"):
#     if unit == "metric":
#         b = weight / (height ** 2)
#     else:
#         b = weight * 703 / (height ** 2)
    
#     return round(b, 2)

# bmi_1 = bmi(70, 1.75)
# print(bmi_1)

# bmi_2 = bmi(154, 69, "imperial")
# print(bmi_2)

# bmi_3 = bmi(60, 1.65)
# print(bmi_3)



# def analyse_scores(scores):
#     avg = sum(scores) / len(scores)
#     high = max(scores)
#     low = min(scores)
#     passed = [s for s in scores if s >= 50]

#     return avg, high, low, len(passed)


# data = [88, 45, 72, 33, 91]

# avg, high, low, pass_count = analyse_scores(data)

# print(f"Average : {avg:.2f}")
# print(f"High : {high}")
# print(f"Low : {low}")
# print(f"Total passed : {pass_count}")
# print(f"Pass % : {(pass_count / len(data)) * 100:.2f}")



# def train_test_split(data, test_size=0.2):
#     n = len(data)
#     split_at = int(n * (1 - test_size))
#     train_data = data[:split_at]
#     test_data = data[split_at:]

#     return train_data, test_data

# dataset = [1,2,3,4,5,6,7,8,9,10]

# train, test = train_test_split(dataset)

# print(f"Train: {train}")
# print(f"Test : {test}")
# train, test = train_test_split(dataset, test_size=0.3)
# print(f"Train: {len(train)} samples, Test: {len(test)} samples")



# def normalise(val, min_val, max_val):
#     return f"{(val-min_val)/(max_val-min_val):.2f}"

# value = float(input("Enter value: "))
# max_value = float(input("Enter max value: "))
# min_value = float(input("Enter min value: "))

# normal = normalise(value, max_value, min_value)
# print(normal)



# def get_grade(marks):
#     if marks >= 80:
#         return "A Grade"
#     elif marks >= 60:
#         return "B Grade"
#     elif marks >= 50:
#         return "C Grade"
#     else:
#         return "F Grade"



# def grade_report(students): 
#     print(f"\n{'Name':12} {'Marks':>6} {'Grade':>6} {'Status':>8}")
#     print("-" * 36)
#     for s in students:
#         g = get_grade(s["marks"])
#         status = "Pass" if s["marks"] >= 50 else "Fail"
#         print(f"{s['name']:12} {s['marks']:>6} {g:>6} {status:>8}")

# class_data = [ {"name":"Krish", "marks":88}, {"name":"Shivam", "marks":45}, {"name":"Dhirendra", "marks":72}, ]
# grade_report(class_data)



# def print_func(x):
#     print(x)

# print_func(5)

# dataset = [ {"name":"Krish", "marks":88}, {"name":"Shivam", "marks":45}, {"name":"Dhirendra", "marks":72}, ]
dataset = {"name" : ["krish", "Shivam", "Dhirendra"], "marks" : [88, 45, 72]}

def load_data():
    print("Loading Data...")
    return dataset

def preprocess(data):
    print("Data is preprocessing...")
    return data

def analyse(data):
    print("Analysing Data...")
    for i in range(len(dataset)):
        if data['marks'][i] >= 80:
            return f"{data['name'][i]} --> Grade: A"
        elif data['marks'][i] >= 60:
            return f"{data['name'][i]} --> Grade: B"
        elif data['marks'][i] >= 50:
            return f"{data['name'][i]} --> Grade: C"
        else:
            return f"{data['name'][i]} --> Grade: F"


results = analyse(preprocess(load_data()))

def report(results):
    print(results)

report(results)