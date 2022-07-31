import mysql.connector as conn


mydb = conn.connect(host = "localhost" , user ="root" , passwd = "pwd" )
cursor = mydb.cursor()

cursor.execute("select employe_id , emp_mailid from saqlain.tcs")

for i in cursor.fetchall():
    print(i)