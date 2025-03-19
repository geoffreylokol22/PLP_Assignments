# Assignment 2: Polymorphism Challenge - Animals

class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        pass  # To be overridden by subclasses

class Dog(Animal):
    def move(self):
        print(f"{self.name} is running.")

class Fish(Animal):
    def move(self):
        print(f"{self.name} is swimming.")

class Bird(Animal):
    def move(self):
        print(f"{self.name} is flying.")

# Animal example
dog = Dog("Buddy")
fish = Fish("Goldie")
bird = Bird("Tweety")

animals = [dog, fish, bird]

for animal in animals:
    animal.move()