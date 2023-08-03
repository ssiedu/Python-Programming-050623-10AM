try:
    num=int(input("Enter any number :"))
    assert num%2==0
except:
    print("Invalid Input")
else:
    r=1/num
    print("Reciprocal of a number :",r)
    
