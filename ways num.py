import numpy as np

arr=np.array([1,2,3,4,5],int)#in numpy specifying type of array is not necessary however you can specify it after writing the array as([1,2,3,4,5],int)
print(arr)

print(arr.dtype)#checks the type of array

arr1=np.array([1,2,3,4,5.0])#python covnvets all of them into float as all of them should be in same data type
print(arr1)

arr2=np.array([1,2.0,3.4,3],int)#converts all of them into int
print(arr2)

#another way of creating array
x=np.linspace(0,16)#array starts from 0 and 16 is also included in the array
print(x)
y=np.linspace(0,16,10)#yeh ham bol rahe hein ke 0 to 16 range ko 10 parts mein divide karo agar 3rd paramenter nahi diya toh by default yeh usko 2nd parameter ke equal mein todega
print(y)
#in linspace spacing between 2 elements is fixed

arr3=np.arange(1,16,3)#print 1 to 16 by skipping 3-3 elements
print(arr3)

arr5=np.logspace(1,15,5)#in log space it also divides the arrays in parts but the parts are not fixed
print(arr5)

arr6=np.zeros(5)
print(arr6)

arr7=np.ones(5)
print(arr7)