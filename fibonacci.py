
n=int(input('enter the number upto which you want the series'))

def func(n):
    a,b=0,1
    for i in range(0,n):
      c=a+b
      print(c,end="  ")
      a=b
      b=c
func(n)
print()

#another process
n1=int(input('enter the value upto you want the series'))
def funcc(n):
     a=0
     b=1

     if(n==1):
        print(a)
     elif n<1:
        print('invalid ')
     else:
        for i in range(0,n):
            
            c=a+b
            print(c)
            a=b
            b=c

funcc(n1)








