class Addition:
    def getdata(self):
        self.__num1=eval(input("Enter First Number :"))
        self.__num2=eval(input("Enter Second Number :"))
    def calAdd(self):
        self.add=self.__num1+self.__num2
    #def display(self):
        print("Addition is :",self.add)


A=Addition()
A.getdata()
A.calAdd()
#A.display()
#print(A.__num1)
A1=Addition()
A1.getdata()
A1.calAdd()
