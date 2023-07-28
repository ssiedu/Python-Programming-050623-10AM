class Base:
    def __init__(self):
        self.num1=eval(input("Enter First Number :"))
        self.num2=eval(input("Enter Second Number :"))


class child1(Base):
    def calAdd(self):
        self.add=self.num1+self.num2
        print("Addition is :",self.add)


class child2(Base):
    def calMul(self):
        self.mul=self.num1*self.num2
        print("Multiplication is :",self.mul)

class child3(Base):
    def calDiv(self):
        self.div=self.num1/self.num2
        print("Division is :",self.div)

c1=child1()
c1.calAdd()
c2=child2()
c2.calMul()
c3=child3()
c3.calDiv()
