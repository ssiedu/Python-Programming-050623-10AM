from multipledispatch import dispatch

@dispatch(int,int)
def product(fnum,snum):
    result=fnum*snum
    print("product of two int value :",result)

@dispatch(float,float)
def product(fnum,snum):
    result=fnum*snum
    print("product of two float value :%.2f"%result)

@dispatch(int,float)
def product(fnum,snum):
    result=fnum*snum
    print("product of two different type of value :",result)

@dispatch(int,int,int)
def product(fnum,snum,tnum):
    result=fnum*snum*tnum
    print("Product of three int value :",result)




product(11,2,3)
product(2.2,1.3)
product(10,2.1)
product(10,2)




    
