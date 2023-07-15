for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()
print("------------------------------------")

#while inside for

for i in range(1,6):
    j=1
    while j<6:
        print("@",end=" ")
        j=j+1
    print()
print("-------------------------------------")

# for inside while

i=1
while i<6:
    for j in range(1,6):
        print("$",end=" ")
    i=i+1
    print()
print("----------------------------------------")

# while inside while

i=1
while i<6:
    j=1
    while j<6:
        print("#",end=" ")
        j=j+1
    i=i+1
    print()




