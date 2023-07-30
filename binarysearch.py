pos=-1  #global
list=[5,8,4,6,9,2]
n=9


def binarysearch(list,n):
    l = 0
    h = len(list) - 1
    while(l<=h):
        mid=(l+h)//2

        if list[mid]==n:
            globals()['pos']=mid
            return True

        elif list[mid]<n:
            l=mid+1

        else:
            h=mid-1


if binarysearch(list,n):
    print('found at ',pos)
else :
    print('not found')