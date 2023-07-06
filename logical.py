num1=int(input("Enter First Number :"))#10
num2=int(input("Enter Second Number :"))#22
print("AND    :",(num1>num2 and num1==num2))#False
print("OR     :",(num1<num2 or num1>=num2))#True
print("NOT    :", not(num1!=num2))#False
print("AND NOT:", not((num1==num2) and (num1<num2)))#True
print("OR NOT :", not(num1<num2) or (num1>=num2))#False
print("AND OR NOT :", not((num1<num2 and num1==num2)or(num1>num2)))
#True
