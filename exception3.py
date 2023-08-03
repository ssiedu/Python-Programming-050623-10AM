try:
    print("Try Block")
    a=int(input("Enter First Number :"))
    b=int(input("Enter Second Number :"))
    c=a/b
except:
    print("In Except Block")
    print("Some Error Occured")
else:
    print("Else Block")
    print("value of c :",c)
finally:
    print("Finally Block")
    print("Program Executed")
