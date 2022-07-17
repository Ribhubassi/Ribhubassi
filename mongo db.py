import pymongo
mongodb+srv://Ribhubassi:@ribhu.zen4q.mongodb.net/?retryWrites=true&w=majority
print(db)


d={
    "name":"ribhu",
    "email":"Ribhubassi25@gmail .com",
    "surname":"Bassi"

}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )

