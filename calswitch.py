while True:
    Uc=input('''Start Calculation
1.Yes('Y'/'y')
2.Exit('N')
''')
    if Uc=='Y' or Uc=='y':
        print('''Select Any One:-
1.Addition
2.Subtraction
3.Multiplication
4.Division
''')
        fnum=eval(input("Enter First Number :"))
        ch=input("Enter Symbol like +,-,*,/ :")
        snum=eval(input("Enter Second Number :"))
        match ch:
            case '+':
                add=fnum+snum
                print("Addition-")
                print("{} + {} = {}".format(fnum,snum,add))
            case '-':
                sub=fnum-snum
                print("Subtraction-")
                print("{} - {} = {}".format(fnum,snum,sub))
            case '*':
                mul=fnum*snum
                print("Multiplication-")
                print("{} * {} = {}".format(fnum,snum,mul))
            case '/':
                div=fnum/snum
                print("Division-")
                print("{} / {} = {}".format(fnum,snum,div))
            case _:
                print("Please Enter Valid Choice ")
    else:
        break

print("Thank You")
        
