# we have earlier printed the array or list elements using loops
#iterator is another method to print the values

nums=[1,2,3,4]
it=iter(nums)# we are creating iterator named it  with function iter and passing list to it
#iterator will give one value at a time

print(it.__next__()) # as when only it is passed it will print the address of it


print(it.__next__())#while calling the next element it will know the last value of i behind the scene

#another way of printing

print(next(it))

print()

for i in nums:# here it will print from beginning
    print(i)

print()
#for our own class and object without inbuild function

class topten:
    def __init__(self):
        self.num=1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num<=10:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration  #to stop the for loop after 10.otherwise it will print none

values=topten()
print(values.__next__())
print(values.__next__())

for i in values:
 print(i)