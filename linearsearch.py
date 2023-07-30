#easy way
# from numpy import*
# arr=array([5,8,4,6,9,2])
# x=len(arr)
# for i in range(x):
#     if arr[i]==9:
#         print("element found at index ",i)

#another way
pos=-1  #global
list=[5,8,4,6,9,2]
n=9

def search(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
           globals()['pos']=i   #local

           return True
        i=i+1


    return False




if search(list,n):
    print('found at ',pos)
else :
    print('not found')