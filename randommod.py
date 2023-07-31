import random
while True:
    uc=input('''Start
1.Yes('y')
2.No('n')
''')
    if uc.lower()=='y': #or uc=='Y':
        com_input=random.randrange(1,6)
        user_input=int(input("Enter any Number :"))
        if com_input>user_input:
            print("computer input :",com_input)
            print("your guess number is smallest number")
        elif user_input>com_input:
            print("Computer input :",com_input)
            print("Your guess number is largest number")
        else:
            print("Computer input : ",com_input)
            print("Both are Equal")
    else:
        break;
