class car:

   wheels=4#this will be common to all objects .this is called as class variables or static variables

   def __init__(self):
        self.milage=10 #this are called as instance variable.i.e this have different values for different objects
        self.brand="bmw"#variables inside init becomes instance variables.variables outside init are class variables



c1=car()
c2=car()

print(c1.milage)
print(c2.milage)

c1.milage=20
print(c1.milage ,c1.wheels,car.wheels)#we can call the class variable by the object as well as the class
print(c2.milage ,c2.wheels,car.wheels)

#now if we want to change value of class variable, we have concept of namespace.
#namespace is the area where you create and store object/variable
#there are two namespace
#class namespace- to store class variables
#object/instance namespace-to store the instance variable

car.wheels=6 #we need to change the value of class variable with help of class
print(c1.wheels,c2.wheels)