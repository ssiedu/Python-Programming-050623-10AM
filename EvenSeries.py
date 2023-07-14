n=int(input("Enter any number :"))
i=int(input("Enter Start number :"))
sum=0
while i<=n:
    #if i%2!=0:
    print(i,end=" ")
    sum=sum+i
    i=i+1
print("\nSum of Even Numbers :",sum)
