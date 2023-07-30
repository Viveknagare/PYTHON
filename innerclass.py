class student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        self.lap=self.laptop()

    def show(self):
        print(self.name,self.roll)
        self.lap.show()

    class laptop:#object of this class must be created in outer class

        def __init__(self):

          self.brand="hp"
          self.ram="16gb"


        def show(self):
            print(self.brand,self.ram)




s1=student('vivek',46)
s2=student('john',20)


s1.show()
s2.show()

print(s1.lap.ram)#we can access the inner class like this

#for creating another object

lap1=s1.lap
lap2=s2.lap

print(id(lap1))
print(id(lap2))

#another way of creating its object

lap1=student.laptop()

#you can create object of inner class inside the outer class
# you can create object of inner class outside the outer class provided you use outer class name to call it

s1.show()




