def bubblesort(arr,x):
    for i in range(n):
        swapped=False
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                swapped=True
                
        if swapped!=True:
            break



list=[22,43,2,56,75]
x=43
n=len(list)

bubblesort(list,x)
print('the sorted list is ',list)
