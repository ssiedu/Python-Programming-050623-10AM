class Addition:
    def __init__(self,a=0,b=0):
        self.num1=a
        self.num2=b
    def calAdd(self):
        self.add=self.num1+self.num2
    def display(self):
        print("Addition :",self.add)


x=int(input("Enter First number :"))
y=int(input("Enter Second Number :"))
A=Addition(x,y)
A.calAdd()
A.display()
A1=Addition(x)
A1.calAdd()
A1.display()
