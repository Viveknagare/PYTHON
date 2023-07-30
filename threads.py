from threading import *
from time import *


#if default every execution has one thread.it is known as MAIN thread
#if we want to execute multiple processes simultaneously on multiple core we create threads
class hello(Thread):#it will create a new thread
    def run(self):
        for i in range(5):
            print('hello ')
            sleep(1)
            def play():
                playsound(beep.mp3)

class hii(Thread):#ir will also create a new thread
    def run(self):
        for i in range (5):
            print('hii ')
            sleep(1)

t1=hello()
t2=hii()

#if we want to print hello and hii with two different threads then the hello needs to be subclass of thread

t1.start()#here thread has run method internally which runs when we call start
sleep(0.5)
t2.start()#same  as above
#now two threads are created which will run simultaneosly
#hii hello will get print simultaneously,but system is so fast that it will run 10 hellos hiis in its one scheduling time therefore we will make it sleep
#some times collision of thread occur due to which hii hello is prited simultaneously
t1.join()#join keeps waiting the main thread until the execution of other threads get over
t2.join()

print('bye')#this will get executed by main thread'