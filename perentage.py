per=eval(input("Enter percentage of student :"))
if per>=80 and per<=100:
    print("A Grade")
elif per<80 and per>=70:
    print("B Grade")
elif per<70 and per>=60:
    print("C Grade")
elif per<60 and per>=50:
    print("D Grade")
elif per<50 and per>=40:
    print("E Grade")
elif per<40 and per>=0:
    print("Fail")
else:
    print("Not valid input")
