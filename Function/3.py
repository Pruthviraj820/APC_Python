class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal created: {self.name}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name) 
        self.breed = breed
        print(f"Dog created: {self.breed}")


d=Dog("Tommy","golden retriver")
