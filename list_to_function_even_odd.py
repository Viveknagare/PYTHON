def func(lst):
    odd,even=0,0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1

    return odd,even

list=[1,2,3,4,5,6]
odd,even=func(list)

print(odd)
print(even)
print()
print('odd:{} and even:{}'.format(odd,even))

