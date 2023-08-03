try:
    a=int(input("Enter First Number :"))
    b=int(input("Enter Second Number :"))
    c=a/b
    print("value of c :",c)
except ZeroDivisionError:
    print("Divide by zero not allowed")
except TypeError:
    print("Type Mismatch")
except ValueError:
    print("Please Enter valid input")
