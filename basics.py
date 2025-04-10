a = 5
b = 6 
x = 1 
y = 2


class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return "Woof!"

my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.name) # Output: Buddy
print(my_dog.breed) # Output: Golden Retriever
print(my_dog.bark()) # Output: Woof!


class Plane:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def fly(self):
        return 'Engines Go!'
    
g5 = Plane('G5', "Twin Jet")
print(g5.name, g5.type, g5.fly())