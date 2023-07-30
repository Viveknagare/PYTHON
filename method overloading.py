#python does not have concept of method overloading
#in a class 2 methods with same name and different parameters

class student:

     def __init__(self,m1,m2):
         self.m1=m1
         self.m2=m2


     def add(self,m1,*m2):#here if we pass more than 2 parameters we can use variable length argument
         s=m1
         for i in m2:
             s=s+i
         print(s)


     def add1(self,m1=None,m2=None,m3=None):
           s=0
           if m1!=None and m2!=None and m3!=None:
             s=m1+m2+m3
           elif m1!=None and m2!=None:
             s=m1+m2
           else:
             s=m1

           print(s)
         #instead of method overloding by defining two functions with same name is not allowed then we managed it in one method

s1=student(12,22)

s1.add1(2)#here now we can pass any number of parameters out of 3




