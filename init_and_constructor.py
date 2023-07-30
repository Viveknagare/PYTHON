class computer:
    pass

c1=computer()
c2=computer()#object is created in heap memory each object have different address
print(id(c1))
print(id(c2))
#size of object depends on the no of variables and size of the variables.and constructor performs the task of assigning the memory


class student:
    def __init__(self):
        self.name='vivek'
        self.age=20


    def update(self): #we use self because self is like a pointer we will not get confuse between the objects
        self.age=40


c1=student()
c2=student()



c2.name='john'
c2.age=20

c2.update()

print(c1.name)
print(c2.name)


#if we want to compare two objects

class client:
    def __init__(self):
        self.name='vivek'
        self.age=20


    def compare(self,c2):
        if self.name==c2.name:
            return True
        else:
            return False





c1=client()
c2=client()

if c1.compare(c2):
    print("they are same")
else:
    print('they are different')



