class pycharm:
    def execute(self):
        print('compiling')
        print('running')

class netbeans:
    def execute(self):
        print('compiling in netbeans')
        print('executing in netbeans')

class Laptop:
    def code(self,ide):#here we can change the type of ide provided we have the method execute.whichever class object you pass that that class must have execute method
        ide.execute()#here we are concern that we have object ide and that class object must have execute method

ide=netbeans()
ide1=pycharm()

lap1=Laptop()
lap1.code(ide)
lap1.code(ide1)
