class Student:
    def get(self):
        self.name=input("Enter name=")
        self.age=int(input("Enter age="))

    def disp(self):
        print("Name=",self.name)
        print("Age=",self.age)

s=Student()
s.get()
s.disp()