num1=eval(input("Enter First Number :"))
num2=eval(input("Enter Second Number :"))
if num1!=num2:
    print(num1," is not equal to",num2)
    if num1>num2:
        print(num1, " is greater than ",num2)
    else:
        print(num2," is greater than ",num1)
else:
    print(num1," is equal to ",num2)
