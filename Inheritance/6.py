class Grand:
    def getg(self):
        print("this is grandfather")

class Father(Grand):
    def getf(self):
        print("this is parent class")

class Child(Father):
    def getc(self):
        print("this is child class")

c=Child()
c.getg()
c.getf()
c.getc()