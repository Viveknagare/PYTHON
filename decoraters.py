# def function():
#  print('hello world')
#
#  func=function#in pythons functions are objects so we can assign one function to another
#  del function #if we delete the function it will not affect the output as its copy is already created in func
#  func()

# def func1(num):
#     if num==0:
#         return print
#     elif num==1:
#         return int  #ek function se ham ek function bhi return kar sakte hein
#
# a=func1(0)
# print(a)


# def func2(func):
#     func("hello")
#
# func2(print)


def dec1(func):#toh dec 1 mein jo bhi pass karenge woh function change hoga according to inner function thus we changed studentDetails without touching it with the help of decoraters
  def inner():
    print("hello good morning")
    func()
    print("thankyou for having us")
  return inner

@dec1
def studentDetails():
    print("your name is vivek")
    print("your age is 20")

# studentDetails=dec1(studentDetails)
# studentDetails()

#this is the way of calling a function another way is to write @function name above the function which is to be passed
studentDetails()

#use-when we need to make same change in many functions then we make a decorater and assign it to every function