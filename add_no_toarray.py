from numpy import *
arr =array([1,2,3,4,5])
arr1=zeros(5)
print(arr1)

for i in range(0,5):#adding with the help of loop
    arr1[i]=arr[i]+5

print(arr1)

arr1=arr1+5#adding directly
print(arr1)

x=array([1,2,3,4,5])
y=array([1,2,3,4,5])
z=x+y
print(z)#adding two arrays

print(concatenate([x,y]))