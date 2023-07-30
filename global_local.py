a=20
def func():
    a=10
    print(a)

func()
print(a)
print()

x=10
def func1():
    global x
    x=20

    print(x)

func1()
print(x)

print()

p=20
print(id(p))
def func2():
    p=10
    print('local p',p)
    x=globals()['p']
    print(id(x))
    print('global p',x)
    x=globals()['p']=5
    print('changed value',x)
    print(id(x))#id will get changed


func2()




