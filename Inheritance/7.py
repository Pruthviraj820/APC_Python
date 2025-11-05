class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Father(Human):
    def __init__(self,name,age):
        super().__init__(name,age)

    def getf(self):
        print("Father goes to work")

class Mother(Human):
    def __init__(self,name,age):
        super().__init__(name,age)

    def getm(self):
        print("Mother can cook")

class Aryan(Father,Mother):
    def __init__(self,name,age):
        super().__init__(name,age)

    def geta(self):
        print("Aryan can't code")

class Gojo:
    def getg(self):
        print("Gojo can code")

class Child(Aryan,Gojo):
    def __init__(self,name,age):
        super().__init__(name,age)
    
    def getc(self):
        print("child is solving leetcode in html")

c=Child("aru",19)
c.getf()
c.getm()
c.geta()
c.getg()
c.getc()