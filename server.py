import socket

s=socket.socket()#we are creating a socket s from module socket using the function socket().here we have not passed anything
#bydefault 1st parameter will be ipv4 and second parameter will be ipv6
print('socket created')
s.bind(('localhost',9999))#here we are binding socket with a port number.because machine will have its own ip we will have to define the portnumber
#port no ranges from 0 to 65535.#server job is to bind socket with the port number.client will simply connect is
#bind takes only one argument therefore we put them in one bracket

s.listen(3)#server will accept only three connections.that is it has capacity to accept only three connections
print('waiting for connections')

#if we want to keep executing the requests of the clients then
while True:
   c,addr= s.accept()#server will accept client connection and server will get two values from it socket and address of the client
   # c is client socket and s is server socket
   name=c.recv(1024).decode()
   print('connected with',addr,name)
   c.send(bytes('welcome to telusco','utf-8')) #we will have to send it in binary format.unicode transformation format.it is variable length character encoding that can represent any characters
   c.close()