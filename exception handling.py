#3 typesof error
#1)compile time error-syntax error 2)run time error-eg divide by zero,users mistake 3)logical error-eg 3+3=5,bugs
a=10
b=5

try:
    print('resource opened')
    print(a/b)
    a=int(input('enter a number'))
    print(a)
    print('resource closed')
except ZeroDivisionError as e:#this block we get executed when there is error
    print("you cannot divide by zero error name is-  ",e)

except ValueError as e:#different types of error have different except blocks
    print('you cannot enter string value ',e)

except Exception as e:
    print('something went wrong')

finally:#it will get executed even if we get error or not
    print('resource closed')
