file=open("Myfile2.txt","w")
name=input("Enter any Name :")
rno=int(input("Enter Roll Number :"))
per=eval(input("Enter Percentage :"))
res= name +"\t"+str(rno)+"\t"+str(per)
file.write("\n"+res)

file.close()
