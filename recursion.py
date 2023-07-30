#by default recursion can be done for 1000 times.we can get it over 1000 by making some customizations.python makes it execute 1000 times and takes care that our system doesnt hang
import sys

print(sys.getrecursionlimit())

#to set the recursion limit.by default it is 1000
sys.setrecursionlimit(2000)

print(sys.getrecursionlimit())

i=0
def recursionlimit():
    global i
    i+=1
    print('limit', i)
    recursionlimit()


recursionlimit()

