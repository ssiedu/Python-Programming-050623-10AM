d1={1:100,2:300,3:400}
d2={1:500,2:600,4:700}
d3={}
d3.update(d1)
print(d3)
d3.update(d2)
print(d3)
for i,j in d1.items():
    for x,y in d2.items():
        if i==x:
            d3[i]=j+y

print(d3)
