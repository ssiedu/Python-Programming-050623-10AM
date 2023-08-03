try:
    a=10
    b=0
    c=a/b
    print("value of c:",c)
except ZeroDivisionError:
    print("Some Error Occured")
except TypeError:
    print("Type Mismatch")
except:
    print("Error : 404 Server not found")
