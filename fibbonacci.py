def fibbonacci(n):
    x=0
    y=1
    print(x)
    print(y)
    i=2
    while i<n:
        z=x+y
        print(z)
        x=y
        y=z
        i=i+1

n=int(input("Enter any number :"))
fibbonacci(n)
