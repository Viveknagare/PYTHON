#now if we want to fetch data from one file and write it in another
f1=open('data','r')
f2=open('abc','w')

for data in f1:
    f2.write(data)

#by default file works in character format but if we have to add image .image
#image contains 0's and 1's so we will have to switch in binary format

f3=open('face-600x900.png','rb')#rb means read binary
f4=open('mypic.JPG','wb')

for i in f3:
     f4.write(i)