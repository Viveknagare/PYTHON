from functools import reduce

def iseven(n):
    return n%2==0

list1=[1,2,3,4,5,6,7,8]
evenlist=list(filter(iseven,list1))
print(evenlist)

#this can be done easily by lambda function as we need the function only for the filter function

evenlist1=list(filter(lambda a:a%2==0,list1))
print(evenlist1)
#filter()function is used to get the values according to our need and parameter we pass

doubles=list(map(lambda n:n*2,evenlist1))
print(doubles)

sum=reduce(lambda a,b:a+b,doubles)
print(sum)