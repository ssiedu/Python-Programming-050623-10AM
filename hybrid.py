class Base:
    def __init__(self):
        self.l=eval(input("Enter length of rectangle :"))
        self.b=eval(input("Enter breadth of rectangle :"))

class Parent1(Base):
    def calRect(self):
        self.area=self.l*self.b

class Parent2:
    def getdata(self):
        self.r=eval(input("Enter radius of circle :"))
    def calCircle(self):
        self.carea=3.14*self.r**2

class child(Parent1,Parent2):
    def display(self):
        print("Area of rectangle :",self.area)
        print("Area of circle    :",self.carea)



c=child()
c.calRect()
c.getdata()
c.calCircle()
c.display()





