import pymongo

client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d ={ "name" : "snigdha" , "email" : "snigdha@gmail.com" , "surname" : " satyajit"}

db1 = client['mongotest']
coll = db1['test1']
coll.insert_one(d)


d2 ={ "name" : "snigdha" , "email" : "snigdha@gmail.com" , "surname" : " satyajit"}

db2 = client['mongotest2']
coll = db2['test2']
coll.insert_one(d2)
