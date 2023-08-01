file=open("Myfile3.txt","w")
for i in range(5):
    name=input("Enter Student Name :")
    rno=int(input("Enter Roll Number :"))
    per=eval(input("Enter Percentage :"))
    cls=int(input("Enter Standard :"))
    data=name+ "  " +str(rno)+"  "+str(per)+"  "+str(cls)+"\n"
    file.write(data)

file.close()
