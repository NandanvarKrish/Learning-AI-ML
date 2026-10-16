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

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def greet(self):
#         return f"Hello {self.name}, Your age : {self.age}"
#
# class Student(Person):
#     def __init__(self, name, age, marks):
#         super().__init__(name, age)
#         self.marks = marks
#
#     def greet(self):
#         base = super().greet()
#         return f"{base}, Your marks: {self.marks}"
#
# class Teacher(Person):
#     def __init__(self, name, age, subject):
#         super().__init__(name, age)
#         self.subject = subject
#     def greet(self):
#         base = super().greet()
#         return f"{base}, Your subject:{self.subject}"
#
#
# s1 = Student("Krish", 18, 95)
# t1 = Teacher("Sam", 24, "AI/ML")
# print(s1.greet())
# print(t1.greet())

# class Student:
#     def __init__(self, name, age, marks):
#         self.name = name
#         self.age = age
#         self._marks = marks
#
#     @property
#     def marks(self):
#         return self._marks
#
#     @marks.setter
#     def marks(self, value):
#         try:
#             if not 0 <= value <= 100:
#                 raise ValueError(f"{value} is out of range")
#
#         except ValueError as e:
#             print(f"Error:{e}")
#
#         else:
#             print(self._marks)
#
#         self._marks = value
#
#     @property
#     def grade(self):
#         if self._marks >= 80:
#             return 'A'
#         elif self._marks >= 50:
#             return 'B'
#         else:
#             return 'F'
#
#
# s = Student("Krish", 18, 98)
#
# print(f"Name  : {s.name}")
# print(f"Age   : {s.age}")
# print(f"Marks : {s.marks}")
# print(f"Grade : {s.grade}")


class Layer:
    def __init__(self, name):
        self.name = name
        self.built = False

    def forward(self ,x):
        raise NotImplementedError("Subclass must implement forward()")

    @property
    def is_built(self):
        return self.built

class ReLULayer(Layer):
    def __init__(self):
        super().__init__("relu")
        self.built = True

    def forward(self, x):
        return [max(0, v) for v in x]

class SigmoidLayer(Layer):
    def __init__(self):
        super().__init__("sigmoid")
        self.built = True

    def forward(self, x):
        return [1 / (1 + 2.718 ** (-v)) for v in x]

relu = ReLULayer()
sigmoid = SigmoidLayer()
print(relu.forward([-2, 0, 3]))


