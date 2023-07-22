def Addition():
    num1=eval(input("Enter First Number :"))
    num2=eval(input("Enter Seond Number :"))
    add=num1+num2
    print("Sum is :",add)

n=int(input("Enter limit :"))
for i in range(n):
    Addition()
