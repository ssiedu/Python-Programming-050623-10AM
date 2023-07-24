n=int(input("Enter any number :"))#11
flag=0
i=2
while i<=(n//2):
    if n%i==0:  
        flag=1
        break;
    i=i+1

if flag==1:
    print("Not prime")
else:
    print("Prime number")
