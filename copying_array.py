from numpy import*
arr1=array([1,2,3,4,5])
arr2=arr1
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))

print()
#this upper two arrays are with same address.this is called as aliasing as both are the same array

arr3=array([3,4,5,6,7])
arr4=arr3.view()#this view creates a new array with different address
print(id(arr3))
print(id(arr4))
print()
print()

#shallow copying-changing value of one array changes the value of other copied array to
arr1[1]=40
print(arr1)
print(arr2)

#deep copy - changing the value of one array doesnt change the value of other array.in this instead of view() use copy()
arr5=array([1,2,3,45])
arr6=arr5.copy()
print(id(arr5))
print(id(arr6))#here too both have different address
arr5[2]=77
print(arr5)
print(arr6)#so by using copy function it copies it deeply thus change in one array doesnt affect the other array.also addressses of both the arrays are different
#in view() we use shallow copy
#in copy() we use deep copy