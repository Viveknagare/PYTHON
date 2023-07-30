#there are some issues with iterator that we have to make the iterator by defining the two functions
#generator will give you iterator

def topten():

    yield 1 #due to this keyword our function becomes generator.and generator gives iterator
            #here return 5 will make the function normal but iterator makes it generator
    yield 2
    yield 3
    yield 4


values=topten()#object of generator.here generator will give iterator
print(values)
print(values.__next__())
print(values.__next__())

for i in values:
    print(i)

#yield is same as that of the function but return will terminate the loop and yield will continue the loop
#to print top 10 perfect square
print()

def toptensqr():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n+=1

value1=toptensqr()

for i in value1:
    print(i)

#here we have created iterator using generator.i.e we are itearting one one value from yield at a time
#generator are mainly used when there is list of prgrms loaded in memory and
#we have to process one at a time rather than fetching entire list we use generator as it will yield one value at a time


