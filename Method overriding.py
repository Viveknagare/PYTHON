#method overeiding- two mwthods with same name and same parameters .ofcourse we cannot have two same method in one class.
#but in inheritanace we have two same methods in two different classes.this is allowed and this is called as method overriding

class student:
    def school(self):
        print("vidya bhavana")

class teacher(student):
    def school(self):  #here teacher class has method school inherited but it overrided the school method
        print('pvgs')

t=teacher()
t.school()
