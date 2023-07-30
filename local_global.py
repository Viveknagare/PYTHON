def something():#here preference will always be given to local variable than that of the global varible inside a function
    a=20        #if you dont have local variable then by default it will take value from global varible
    print('in',a)

a=10
something()
print('out',a)
print()


#x=20
def variable():
    global x
    x=10
    print('inside',x)


variable()
x=20
print('outside',x)
#whenever we declared variable as global inside a function the value get assigned to entire scope
#we cannot have both local and global variable inside a same function .once a global variable declared inside a function we cannot make local variable
#so we use concept of globals() function
print()

x = 10
def func():
    x = 15
    print("local x: ",x)
    y = globals()['x']
    print("global x: ",y)
    globals()['x'] = 20

func()