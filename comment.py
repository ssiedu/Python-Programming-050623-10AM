#This is single line comment
print("Single Line Comment ")
'''This is
multiline
comment'''
print("Multiline comment")


def doccmt():
    '''This is docstring comment'''
    print("Hello!")


doccmt()
print(doccmt.__doc__)
