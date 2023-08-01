import pickle
list1=[11,22,33,44,55]
file=open("Myfile6","wb")
pickle.dump(list1,file)
file.close()

file=open("Myfile6","rb")
data=pickle.load(file)
print(data)
file.close()
