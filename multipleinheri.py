class Base1:
    def get_x(self):
        self.x=eval(input("Enter First number :"))


class Base2:
    def get_y(self):
        self.y=eval(input("Enter second Number :"))

class Base3:
    def get_z(self):
        self.z=eval(input("Enter Third Number :"))


class child(Base1,Base2,Base3):
    def calculate(self):
        self.product=self.x*self.y*self.z
        print("Product of three number :",self.product)


C=child()
C.get_x()
C.get_y()
C.get_z()
C.calculate()








        
