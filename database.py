import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="Vivek@1831",database="employeemanagementsystem")

mycursor=mydb.cursor()
mycursor.execute("show databases")
for i in mycursor:
     print(i)

     # instead of usinf mycursor you can store it in another variable

mycursor.execute("select * from login")
result=mycursor.fetchall() #or you can use fetchone to fetch only one value
for i in result:
    print(i)

#here we can use all mysql statements




