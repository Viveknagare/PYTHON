class student:
    def details(self):
        print("vivek 20")

s1=student()
s2=student()
print(type(s1))#this gives keyword class and gives module name as main as we are executing it in the same module itself and gives name of the class
student.details(s1)
student.details((s2))

#in most of the type you will see the syntax

s1.details()
s2.details()

a=6
print(type(a))
print(int.bit_length(a))


#or

print(a.bit_length())