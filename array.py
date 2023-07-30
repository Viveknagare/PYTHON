from array import*
a=array('i',[12,2,32,4,51])
print(a)
print(a.buffer_info())
print(a.typecode)

newarr=array(a.typecode,(a for a in a))#code to copy the array a to new arr
for e in newarr:
    print(e)

    print()

newarr1 = array(a.typecode, (a*a for a in a))  # code to copy the array a to new arr and taking its square
for j in newarr1:
    print(j)

a.reverse()#for reversing the array
print(a)
print(a[0])#printing one value

print()

for i in range(0,5):#various meth0ds to print elements of the array
    print(a[i])

print()

for i in a:
    print(i)

print()
for i in range(len(a)):
    print(a[i])

    print()

i=1
while i<=(len(a)):
    print(a[i])
    i+=1


