#in methods there are three types of methods
# 1.class methods
# 2.static methods
# 3.instance methods
#init method is also called as constructer

class student:

    school="vidya bhavan"

    def __init__(self,subject1,subject2,subject3):
        self.subject1=subject1
        self.subject2=subject2
        self.subject3=subject3


    def avg(self):     #this is the instance method as it works with the object.self matlab object involve hoga use ham instance method bolte hein
        return (self.subject1+self.subject2+self.subject3)/3


    def get_subject1(self):   #this are called as getters/accessors
        return self.subject1


    def set_subject1(self,val):  #this are called as setters/mutators
        self.subject1=val

    @classmethod
    def getschool(cls):
        return cls.school

    @staticmethod
    def info():
        print("school is located in ghatkopar")


s1=student(10,20,30)
s2=student(10,22,32)
#calling instance methods
print(s1.avg())
print(s2.avg())
#accessor-only fetch the value of instance variable

print(s1.get_subject1())

s1.set_subject1(20)
print(s1.subject1)

#calling class method

print(student.getschool())

#when we are not concern about instance variables, not about the class variables ,just we want to do some extra then we use static method

student.info()