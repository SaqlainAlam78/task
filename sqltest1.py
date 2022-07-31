import mysql.connector as conn


mydb = conn.connect(host = "localhost" , user ="root" , passwd = "pwd" )
cursor = mydb.cursor()
cursor.execute("insert into saqlain.tcs values(101 , 'sudhanshu kumar', 'sudhanshu@ineuron.ai' ,100 , 30)")
mydb.commit()
cursor.execute("select * from saqlain.tcs")
for i in cursor.fetchall():
    print(i)
