import pymongo

client = pymongo.MongoClient("mongodb+srv://SaqlainAlam:pwd@cluster0.h3cx6.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

data = {
    "name":"SaqlainAlam",
    "email" : "saqlainalam350@gmail.com",
    "surname" : "Alam",
    "location" : "kolkata"
}

list_of_records = [
    {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Machine Learning with Deployment'},

    {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Deep Learning for NLP and Computer vision'},

    {'companyName': 'iNeuron',
     'product': 'Master Program',
     'courseOffered': 'Data Science Masters Program'}
]

database = client['myinfo']
collection = database["saqlain"]
collection.insert_one(data)




record = collection.find()
for i in record:
    print(i)