def passtuple(tup1):
    '''list1=list(tup1)
    print("List is :")
    print(list1)
    list1.append("orange")
    print(list1)
    tup1=tuple(list1)
    print(tup1)'''


t1=(11,22,33,44,55)
print("Before function call")
print(t1)
passtuple(t1)
print("After function call")
print(t1)
