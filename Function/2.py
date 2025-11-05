from abc import ABC, abstractclassmethod

class Animal(ABC):
    @abstractclassmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Dog barks")


d=Dog()
d.speak()