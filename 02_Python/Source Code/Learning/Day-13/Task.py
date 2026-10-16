# class Student:
#     def __init__(self, name, age, marks):
#         self.name = name
#         self.age = age
#         self.marks = marks
#
#     @property
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
#     @property
#     def is_passed(self):
#         return "Passed" if self.marks > 50 else "Failed"
#
#
# s = Student("Krish", 18, 90)
# print(s.is_passed)
# print(s.grade)
#

# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         return "..."
#
#     def info(self):
#         print(f"{self.name} says: {self.speak()}")
#
# class Dog(Animal):
#     def speak(self):
#         return "Woof!"
#
# class Cat(Animal):
#     def speak(self):
#         return "Meow!"
#
# class Bird(Animal):
#     def speak(self):
#         return "Tweet!"
#
#     def fly(self):
#         print(f"{self.name} is flying!")
#
#
# Dog("Bob").info()
# Cat("Oggy").info()
# Bird("pigeon").info()
# Bird("pigeon").fly()



