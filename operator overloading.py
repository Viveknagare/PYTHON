
#dynamic typing-in these the value given to the variable , python automatically predicts the type of value that is a=9 is int b='vivek' is string
#synthetic sugar- some terms are applied that is we cannot add string and integer as in backend int is a class that takes two parameters in add method

a,b=20,30
print(a+b)
print(int.__add__(a,b))#behind the scenes
#we have different methods for different operators as eg - sign-->__sub__() method
                                                         #* sign-->__mul__() method

#this different methods are called magic methods

class student:
    def __init__(self,marks1,marks2):
        self.marks1=marks1
        self.marks2=marks2



    def __add__(self, other):#here we are overloading the operator with methods as per our need as + operator in backend student class must know to use add method for adding .
        m1=self.marks1+other.marks1
        m2=self.marks2+other.marks2
        s3=student(m1,m2)

        return s3

    def __gt__(self, other):
        s1=self.marks1+self.marks2
        s2=other.marks1+other.marks2

        if s1>s2:
            return True
        else:
            return False

    def __str__(self):
        return "{}  {}".format(self.marks1, self.marks2)



s1=student(50,50)
s2=student(35,35)
s3=s1+s2
print(s3.marks1)
print(s3.marks2)

if s1>s2:
    print('s1 win')
else:
    print('s2 win')


print()

a=20
print(a)
print(a.__str__())#behind the scenes


print(s1.__str__())#this is also calling str which prints the address and not the value. even it is not defined in our class then too is is present in the backend
#as we want values and not the address we will have to override the str method by creating new str method in our class
print(s3) #even if we dont write str it will print value
#but id we remoove the string format than it till give values for s3.__str__ in tuples but not for s3