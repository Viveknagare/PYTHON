def greet():
    print("hello good morning")

def add(x,y):#without return type
    z=x+y
    print(z)

def mul(x,y):
    a=x*y
    return a


greet()
add(5,6)
f=mul(3,4)
print(f)

def sub_div(x,y):
    z1=x-y
    z2=x/y
    return z1,z2

res1,res2=sub_div(12,4)
print(res1)
print(res2)