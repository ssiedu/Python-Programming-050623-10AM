def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

num=int(input("Enter any number :"))
print("factorial is :",factorial(num))