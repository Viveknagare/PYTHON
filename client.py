import socket

c=socket.socket()
c.connect(('localhost',9999))#here we will mention ip address of the server and the port number you want to connect with
#when connection established with the client then clients port number will automatically generated
#when we are doing it on different machines dont forget to write the ip of machine in client instead of localhost
name=input('enter your name')
c.send(bytes(name,'utf-8'))
print(c.recv(1024).decode()) #we have use decode because it will print b in start of the mssg that is bytes
#we will get new port nos that is new users when we will run the client file.client will receive
#client will receive the information and after its turn server will make connection with another client