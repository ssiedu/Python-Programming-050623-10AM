import math
class Base:
    def __init__(self):
        self.r=eval(input("Enter radius of circle :"))


class derive(Base):
    def calArea(self):
        self.area=math.pi*(self.r**2)
        print("Area of circle :%.2f"%self.area)


D=derive()
#D.getdata()
D.calArea()
