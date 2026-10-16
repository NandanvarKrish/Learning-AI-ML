# class Students:
#     def __init__(self, name, age, marks):
#         self.name = name
#         self.age = age
#         self.marks = marks
#
#     def grade(self):
#         if self.marks >= 90:
#             return 'A'
#         elif self.marks >= 80:
#             return 'B'
#         elif self.marks >= 70:
#             return 'C'
#         elif self.marks >= 50:
#             return 'D'
#         else:
#             return 'F'
#
#     def is_passing(self):
#         if self.marks >= 50:
#             return True
#         else:
#             return False
#
#     def report(self):
#         return f"Name: {self.name:5} | Age: {self.age:2} | Marks: {self.marks:2} | Grade: {self.grade():2} |  Is_passed: {self.is_passing()}"
#
# s1 = Students("Krish", 18, 90)
# s2 = Students("Ansh", 17, 60)
# s3 = Students("Arya", 18, 45)
#
# s = [s1, s2, s3]
#
# for student in s:
#     print(student.report())

# class Student:
#     school = "BeaconHouse"
#     pass_marks = 50
#
#     def __init__(self, name, age, marks):
#         self.name = name
#         self.age = age
#         self.marks = marks
#
#     def status(self):
#         if self.marks > Student.pass_marks:
#             return f"Pass at {Student.school}"
#         else:
#             return f"Fail at {Student.school}"
#
#     def grade(self):
#         if self.marks >= 90:
#             return 'A'
#         elif self.marks >= 80:
#             return 'B'
#         elif self.marks >= 70:
#             return 'C'
#         elif self.marks >= 50:
#             return 'D'
#         else:
#             return 'F'
#
#     def is_passing(self):
#         if self.marks >= 50:
#             return True
#         else:
#             return False
#
#     def report(self):
#         return f"Name: {self.name:5} | Age: {self.age:2} | Marks: {self.marks:2} | Grade: {self.grade():2} |  Is_passed: {self.is_passing()}"
#
#
# s1 = Student("krish", 18,88)
# s2 = Student("shivam", 18, 80)
# s3 = Student("anuj", 18, 85)
# s4 = Student("dhiren", 19, 70)
# s5 = Student("satyam",17, 46)
#
# s = [s1, s2, s3, s4, s5]
# s_marks = [s1.marks, s2.marks, s3.marks, s4.marks, s5.marks]
#
# sorted(s, key=lambda s: s.marks, reverse=True)
#
# for student in s_marks:
#     print(student)

# class Classroom:
#     def __init__(self):
#         self.students  = []
#         # self.students = students
#
#     def add_students(self, student):
#         self.students.append(student)
#         print(self.students)
#
#
# s1, s2, s3, s4, s5 = Classroom(), Classroom(), Classroom(), Classroom(), Classroom()
# s1.add_students("krish")
# s2.add_students("shivam")
# s3.add_students("dhiren")
# s4.add_students("atharv")
# s5.add_students("satyam")


# class SimpleClassifier:
#     def __init__(self, threshold = 50):
#         self.threshold = threshold
#         self.trained = False
#         self.n_examples = 0
#
#     def fit(self, X, y):
#         self.n_examples = len(X)
#         self.trained = True
#         print(f"Trained on {self.n_samples} samples")
#         return self
#
#     def predict(self, X):
#         if not self.trained:
#             raise RuntimeError("Call fit() before predict()!")
#
#         return [1 if x >= self.threshold else 0 for x in X]
#
#     def score(self, X, Y):
#         self.X = X
#         self.Y = Y
#         preds = self.predict(X)
#         correct = sum(1 for p, t in zip(preds, y) if p == t)
#         return round(correct / len(y) * 100, 2)
#
# model = SimpleClassifier(threshold=60)
# X = [80, 45, 72, 33, 91]
# y = [1, 0, 1, 0, 1]
# model.fit(X, y)
# print(model.predict([70, 40, 85]))
# print(model.score(X, y))

# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f'{self.name} is {self.age} years old'
#
#
# print(Student('Krish',18))


class Datapipeline:
    def __init__(self, data):
        self.data = data

    def normalise(self):
        return [x/100 for x in self.data]

sample_data = [100, 200, 300, 400, 500]
print(Datapipeline(sample_data).normalise())

