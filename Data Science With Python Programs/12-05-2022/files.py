file_ob=open("abc.txt","w")

print("file created")
#we can create all types of files using file handling

file_ob.write("This file  created using python")
file_ob.close()

#reading files  first we need open the file in the read mode

file_ob=open("abc.txt","r")
text=file_ob.read()
text1=file_ob.read(3)
print(text)
print(text1)
