#the above we saw single level inheritance

class student:#parent class
    def school(self):
        print('pune vidya bhavan')

    def pincode(self):
        print('400075')

class vivek(student): #subclass/childclass
    def fullname(self):
        print('vivek bharat nagare')

    def std(self):
        print('you are in 10th std')

#calling parent class
s1=student()
s1.school()
s1.pincode()

#calling child/subclass
v1=vivek()

v1.school()
v1.pincode()
v1.std()
v1.fullname()



#multilevel inheritance
print()

class A:
    def feature1(self):
        print("feature 1 executed")

class B(A):
    def feature2(self):
        print("feature 2 executed")

class C(B):
    def feature3(self):
        print('feature 3 executed')

a=A()
a.feature1()

b=B()
b.feature1()
b.feature2()

c=C()
c.feature1()
c.feature2()
c.feature3()

print()

#multiple inheritance
class X:
    def firstname (self):
        print('vivek', end=" ")

class Y:
    def lastname(self):
        print("nagare",end=" ")

class Z(X,Y):
    def middlename (self):
        print('bharat', end=" ")


x=X()
x.firstname()
print()

y=Y()
y.lastname()
print()

z=Z()
z.firstname()
z.middlename()
z.lastname()
