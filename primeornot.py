x=int(input('enter a number'))
for i in range(2,x):#code ko more eff banane ke liye ham int(x/2) taak matlaab jo number check karna hein uske half taak hein check krenge
    if x%i==0:
        print('it is not prime no')
        break
else:
  print('it is  a prime number')


#for i in range(2,int(x/2))