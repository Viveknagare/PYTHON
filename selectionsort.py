def selectionsort(arr, x):
    for i in range(0,n-1): #yaha pe loop ham 0 se agar n=5 rahega to 4 taak chalayenge kyuki j=i+1 hein toh j 5 taak jana chaiye i ko agar 5 kiya toh j 6 tak jayega which is out of bound exception
        mid_index=i
        for j in range(i+1,n):
            if arr[j]<arr[mid_index]:     #by this we are we are searching minimum element in the array .
                mid_index = j                          # and in every iteration we are replacing the minimum value by the ith indexx
                                          # that is every iteration we are getting minimum number at the start

        if mid_index!=i:
             temp=arr[i]
             arr[mid_index]=arr[i]
             arr[i]=temp


list = [22, 43, 2, 56, 75]
x = 43
n = len(list)

selectionsort(list, x)
print('the sorted list is ', list)
