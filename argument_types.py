def person(name,age):
    print(name)
    print(age)

person('vivek',20)
print()

#suppose you dont know sequence of function arguments
person(age=20,name='vivek')#here this are called as keywords
print()

#suppose we dont pass value of one parameter the it will take default value
def person1(name,age=18):
    print(name)
    print(age)

person1('vivek')
person1('aachal',50)#here it will override the age
print()

#variable length arguments:user can give no of parameters he wants
def summ(a,*b):#a will accept 1st value other multiple values are accepted by b
    c=a
    for i in b:
        c=c+i

    print(c)


summ(1,34,54,32)#here a takes 1 and b takes rest other values in tuples

#or
print()

def summm(*b):
    c=0
    for i in b:
        c=c+i
    print(c)

summm(1,34,54,32)
