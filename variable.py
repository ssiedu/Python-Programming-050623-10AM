'''def variable_length(*data):
    for i in data:
       #print(i)
    print(data)
    print(data[1])


variable_length(10,20,30,40)'''

def variable_length1(**data):
    for i,j in data.items():
       print(i,j)
    print(data)
    print(data['b'])


variable_length1(a=10,b=20,c=30,d=40)
