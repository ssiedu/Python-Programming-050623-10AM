class Base:
    def getdata(self):
        print("This is Base class function")

class Derive(Base):
    def getdata(self):
        #Base.__init__(self)
        super().getdata()
        print("This is Derive class function")

D=Derive()
D.getdata()

