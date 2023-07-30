from numpy import *
arr=array([[1,2,3,2,3,2],[4,5,6,4,23,2,]])

print(arr)
print(arr.dtype)
print(arr.ndim)#it will give no of dimension
print(arr.shape)#it will give no of rows and columns
print(arr.size)

#conversion of 2d to 1d array
arr1=arr.flatten()
print(arr1)

#from 1d to 2d array conversion
arr2=arr1.reshape(3,4)#passa the no of rows and columns to which you want to convert
print(arr2)
print()
arr3=arr1.reshape(2,2,3)#it will make a 3d array that will have 2 2d arrays with 2 rows and three columns
print(arr3)