class GrandParent:
    def __init__(self):
        self.p=int(input("Enter principle amount :"))
        self.r=int(input("Enter rate of interest :"))
        self.t=int(input("Enter time in year :"))


class Parent(GrandParent):
    def calculate_Si(self):
        self.si=(self.p*self.r*self.t)/100
        self.total=self.si+self.p


class Child(Parent):
    def display(self):
        print("Simple Interest : ",self.si)
        print("Total amount :",self.total)


C=Child()
C.calculate_Si()
C.display()






        
