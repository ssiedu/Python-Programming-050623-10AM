Ram=int(input("Enter age of ram :"))
Shyam=int(input("Enter age of shyam :"))
sita=int(input("Enter age of sita :"))
if Ram<Shyam and Ram<sita:
    print("Ram is Youngest ")
elif Shyam<sita:
    print("Shyam is youngest")
else:
    print("sita is youngest")
