
#1. Create a  table attribute dataset and dress dataset
#2. Do a bulk load for these two table for respective dataset
import pandas as pd
import mysql.connector as conn
import pymongo
import json

client = pymongo.MongoClient("mongodb+srv://SaqlainAlam:yourpwd@cluster0.h3cx6.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

mydb = conn.connect(host = "localhost" , user ="root" , passwd = "yourpwd" ,database="saqlain")
cursor = mydb.cursor()

s = cursor.execute("SHOW TABLES")
for i in cursor.fetchall():
    print(i)

#3. read these dataset in pandas as a dataframe

s = pd.read_csv(r'C:/Users/user/Downloads/Attribute DataSet1.csv')
p = pd.read_csv(r'C:/Users/user/Downloads/Dress Sales1.csv')
print(s)
print(p)

# 4. Convert attribute dataset in json format

a = s.to_json("s_JSON")
b = p.to_json("p_JSON")

#5. Store this dataset into mongodb

database = client['Task']

collection = database["Json"]

print(s)

with open(r'C:\Users\user\PycharmProjects\pythonProject\task123\p_JSON') as file:
    file_data = json.load(file)

if isinstance(file_data, list):
    collection.insert_many(file_data)
else:
    collection.insert_one(file_data)

#6. Try to find out how mnay dress is having recommendation 0

select distinct(Dress_id) from attribute_dataset

#7. Try to find out how mnay dress is having recommendation 0
select count(*) from table name where recommendation = 0

#8. Try to find out total dress sell for individual dress id

dress_sales['Sales'] = dress_sales[['29/8/2013', '31/8/2013', '2/9/2013','4/9/2013','6/9/2013','8/9/2013','10/9/2013',
                                        '12/9/2013','14/9/2013','16/9/2013','18/9/2013','20/9/2013','22/9/2013','24/9/2013'
                                        ,'26/9/2013','28/9/2013','30/9/2013','2/10/2013','4/10/2013','6/10/2013',
                                        '8/10/2013','10/10/2013','12/10/2013']].agg('sum', axis=1)

print(dress_sales.groupby('dress_id')['Sales'].sum())

#9. Try to find out a third highest most selling dress id

SELECT DISTINCT SALES AS 3RDHighestSales
FROM DRESS_SALES_TABLE
ORDER BY SALES DESC
LIMIT 1
OFFSET 2;








