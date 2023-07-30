from numpy import *
arr=array([[1,2,3,4,5,6],[7,8,9,0,1,2]])


m=matrix(arr)
print(m)#output looks exactly similar to print(arr) but here you can perform many operations

#direct matrix without 2d array

m1=matrix('1 2 3 4;5 6 7 8')#string format
print(m1)
print()
m2=matrix('1 2 ;3 4; 5 6;7 8 ')#4 rows 2 columns
print(m2)
print()
print(diagonal(m2))#gives diagonal elements
print()
print(m1.min())#gives min val of matrix
print(m1.max())#gives max value

m3=matrix('1 2;3,4')
m4=matrix('1 2;3 4')
m5=m3+m4
print(m5)
print()
m6=m3*m4
print(m6)

