f=open('data','r')
print(f)
#print(f.read()) gives entire file data
print()
print(f.readline(),end="") #only prints the 1st line and has pointer that moves to next line
print(f.readline(),end="")#it will give spaces in lines because print have new line and data in the file also have new line
print(f.readline(4),)#it will print only 4 characters

#in order to read data
f1=open('abc','w')
f1.write("vivek nagare")
f1.write(" laptop")
f1.write(" hello")#if we remove this then data will get deleted as weare using only the w .

f2=open('abc','a')#here it will append the data

f2.write(' thankyou')




