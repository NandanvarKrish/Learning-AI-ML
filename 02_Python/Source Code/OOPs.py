class Dog:
    @property
    def bark(self):
        print(self.name + " says woof!")

pet = Dog()
pet.name = "Doggy"
pet.age = 2

print(f"Name: {pet.name}")
print(f"Age: {pet.age}")
pet.bark

