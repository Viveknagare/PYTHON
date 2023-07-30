class A:
    def __init__(self):
        print("init of A triggered")

    def feature1(self):
        print("feature1 triggered")

    def feature2(self):
        print('feature2 triggered')

class B(A):
    def __init__(self):
        super().__init__()
        print("init of B triggered")

    def feature3(self):
        print("feature3 triggered")

    def feature4(self):
        print('feature4 triggered')


b1=B()
b1.feature1() #it will find the init metho/constructor firstly in the class he belongs if not present then it will print the init method of parent class
#but if we want to print init of child as well as parent class
#when you create object of subclass it will call the init of  subclass first and then the init of parent class by using the super keyword


#MRO(method resolution order) this can be seen in multiple inheritance

class X:
    def __init__(self):
         print("init of X triggered")

    def featureX(self):
        print("featureX triggered")

    def featureY(self):
        print('featureY triggered')

class Y:
    def __init__(self):
        super().__init__()
        print("init of Y triggered")

    def featureP(self):
        print("featureP triggered")

    def featureQ(self):
        print('featureQ triggered')


class Z(X,Y):
    def __init__(self):
        super().__init__()#here in X and Y init of x is triggered.this follows MRO

        print('init of z triggered')

z=Z()
#firstly it will find the init method in the object class then it will follow the class present in the left side that is !st class which is class a and then 2nd class
#same goes with method if two mwthods present in two different classes having same name , and are called by 3rd class inheriting the properties of 1st and 2nd class then between two it will always choose the left that is 1st method
#super keyword is also used to call other methods
