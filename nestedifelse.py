number=int(input("Enter any number :"))
if number==0:
    print("Zero")
elif number>0:
    print("positive Number")
    if number%2==0:
        print("Even Number")
    else:
        print("Odd Number")

else:
    print("Negative number")
    if number%2==0:
        print("Even Number")
    else:
        print("Odd Number")
