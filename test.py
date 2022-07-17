import pymongo



client = pymongo.MongoClient("mongodb+srv://snigdhasatyajit:<ninny724>@cluster0.hrz48jb.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d ={ "name" : "snigdha" , "email" : "snigdha@gmail.com" , "surname" : " satyajit"}

db1 = client['mongotest']
coll = db1['test1']
coll.insert_one(d)
