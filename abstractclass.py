#by default python does not support abstract class but we can make a class abstract by importing it from abc module that is abstract base class module
#we cannot make object of abstract class
from abc import ABC,abstractmethod

class computer(ABC): # abstract class is a class which have atleast one abstract method

    @abstractmethod
    def process(self):# a abstract method is a method that have no body
        pass

class laptop(computer):
    def process(self):# here we will have to overide the method process as it will not work when the the properties of computer are inherited which have abstract method
        print("process of laptop running")


class programmer(laptop):
    def work(self,com):
        print("solving bugs")
        com.process()



class whiteboard:
    def write(self):
        print('writing on a white board')

    def process(self):
        print('yeah its running')



#com=computer()#we cannot make object of abstract class
com1=laptop()# here we can create object as we have overide the method process
com1.process()

prg=programmer()
prg.work(com1)


wh=whiteboard()
prg.work(wh)

#we can write code without abstract classes but it depends on the design of the software some api follows oop pattern for building software






