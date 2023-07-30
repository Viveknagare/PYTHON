import smtplib

server=smtplib.SMTP('smtp.gmail.com',587)  #host name and port number

server.starttls() #start lets you start the connection#tls is transport layer security or ssl also called as secure socket layer

server.login('vivekbnagare31@gmail.com','ksjt vgli pbrm xqna')#login by username and password.#first on 2 step verification and generate app password this password is used to sent mails using third party apps.this feature has came after the google disanled the less security app option
server.sendmail('vivekbnagare31@gmail.com','shobhabnagare@gmail.com ','code from python')#senders username,receiver username,and mssg are the parameters
print('mail sent')




#smtp-simple mail transfer protocol
#http=hypertext trasnfer protocol to access www
#ftp-file transfer protocol
#tcp/udp-for sending packets