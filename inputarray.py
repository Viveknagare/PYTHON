from array import *
#user array input
arr = array('i',[])
n = int(input('enter the size of the array'))

for i in range(n):
    x=int(input('enter the element you want to insert'))
    arr.append(x)

print(arr)

for i in range(n):
    print(arr[i],end=" ")

print()

    #or

for i in arr:
    print(i,end=" ")

print()

#searching index of a element manually
f=int(input("enter a array element"))
for i in range(n):
    if arr[i]==f:
        print('index of the array element is ',+i)
        break
else:
    print('array element not found')

print()

z=int(input('enter the array element you want to search'))

#direct function
res=arr.index(z)
print( 'index of array element is ',+res)







