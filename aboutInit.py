class computer:
    def __init__(self,ram,cpu):
        self.ram=ram
        self.cpu=cpu
        print("hello")


    def config(self):
        print("config is ",self.cpu,self.ram)

c1=computer("8 gb","hdd")#here when we make object we can directly pass the arguments in the constructor it will go in init function parameters
computer.config(c1) #or c1.config

c2=computer("16gb","ssd")
computer.config(c2) #or c2.config