def update(x):
    x=10
    print(id(x))

update(4)

a=20
update(a)#here it is pass by value i.e we are passing only the value of variable a.it will not affect original value of a
print(id(a))
#in pass by refrence the actual address of the variable is passed due to which change in the value of varible will also affect its original value
#but we dont have like wise such concept in python
#in python the moment we pass a value of variable to the function then both share the same address but when we update the value address gets changed
print()
def update1(x):
    print(id(x))

a=20
print(id(20))
update1(a)
#in this case both will have same address as the the value is not updated both variables will share same address
#so there is no such concept as pass by value and pass by refrence
print()

def update2(lst):
    lst[1]=25
    print(id(lst))
    print(lst)

l1=[10,20,30]
print(id(l1))
update2(l1)#as list is mutable this does not change its address
#but when a value of variable is changed and variable is not mutable thus it assigns new address to the changed value
print(l1)#thus by passing the original one it will print the updated one as both have same address