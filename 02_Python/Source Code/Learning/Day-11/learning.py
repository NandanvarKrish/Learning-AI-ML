# try:
#     age = int(input("Enter your age: "))
#     print(f"Age : {age}")

# except ValueError:
#     print("Please enter a number!")

# try:
#     data = [10, 20, 30]
#     # result = data[5]
#     val = 10/0
#
# except IndexError:
#     print("Index out of range")
#
# except ZeroDivisionError:
#     print("Cannot divide by zero")
#
# except Exception as e:
#     print(f"Unexpected: {e}")

# finally:
#     print("This ALWAYS runs")

# import csv

# try:
    # a = 5
    # # print("5" + a)
    # d = {"name" : "Krish"}
    # print(d['age'])

    # with open("x.csv", "r") as f:
    #     reader = csv.DictReader(f)
    # # LIST = []
    # data = {"name":"Ankit", "marks":49, "grade":"F"}

    # with open("new_config.csv", "a") as f:
    #     w = csv.DictWriter(f, fieldnames=["name","marks","grade"])
    #     w.writeheader()
    #     w.writerows(data)

# except TypeError:
#     print("Type Error!!!")

# except KeyError:
#     print("Key Error!!!")

# except FileNotFoundError:
#     print("File Not Found")
# except Exception as e:
#     print(f"Unexpected: {e}")

# def validate_marks(marks):
#     if not isinstance(marks, (int, float)):
#         raise TypeError(f"Marks must be a number, we received {type(marks)}")
    
#     if marks < 0 or marks > 100:
#         raise ValueError(f"Marks must be between 1-100, we received {marks}")
    
#     return "A" if marks >= 80 else "B" if marks >= 60 else "F"

# for test in [85, 150, "abc", 45]:
#     try:
#         print(f"{test} --> {validate_marks(test)}")
    
#     except (ValueError, TypeError) as e:
#         print(f"❌ {test} : {e}")


# def safe_read(filepath):
#     try:
#         with open(filepath) as f:
#             return f.read()
        
#     except FileNotFoundError:
#         print(f"File not Found: {filepath}")
#         return None
    
#     except PermissionError:
#         print(f"Permission Denied: {filepath}")
#         return None

# def process_dataset(records):
#     results = []
#     errors = 0

#     for i, r in enumerate(records):
#         try:
#             marks = float(r['marks'])
#             status = "Pass" if marks >= 50 else "Fail"
#             results.append({"name":r['marks'], "status" : status})
#         except (KeyError, ValueError) as e:
#             print(f"Row {i} Skipped: {e}")
#             errors += 1
#             print(f"Processed: {len(results)} ok, {errors} errors")
#             return results
    
# data = [{"name" : "krish", "marks" : "88"}, {"name" : "Utkarsh", "marks" : "N/A"}, {"name" : "Shivam"}, {"name" : "Shyam", "marks" : "72"}]
# process_dataset(data)


import csv, json

def load_and_process(filepath):
    results = []
    log = []
    try:
        with open(filepath) as f:
            for i, row in enumerate(csv.DictReader(f)):
                try:
                    marks = float(row['marks'])

                    if not (0 <= marks <= 100):
                        raise ValueError(f"marks  {marks} are out of range")
                    results.append({"name" : row['name'], "marks" : marks, "grade" : "A" if marks >= 80 else "B" if marks >= 60 else "F"})
                except FileNotFoundError:
                    print(F"❌ File not found: {filepath}")
                    return [], []
    finally:
        print(f"✅ Done: {len(results)} processed, {len(log)} errors")
    return results, log
