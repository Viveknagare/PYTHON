
print('hello '+__name__)#if you are executing the file where __name__is present the it will print main
#but same file when imported to another file there it will print module name

def main():
    print('hello')

def greet():
    print('welcome vivek')


if __name__=="__main__":#here we are saying that whenever we will import specialvariable1 to 2 then it will print main() only if satisfies the condition
    main()

greet()