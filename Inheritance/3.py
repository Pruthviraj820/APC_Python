class Vehicle:
    def get(self):
        self.brand=input("Enter brand name=")
        self.model=input("Enter model=")

    def disp(self):
        print("Brand name=",self.brand)
        print("Model number=",self.model)

class Car(Vehicle):
    def car1(self):
        self.year=int(input("Enter Year="))

    def card(self):
        print("Year=",self.year)

c=Car()
c.get()
c.car1()
c.disp()
c.card()
