# Intro to MongoDB
See the [link](https://jslvtr.gitbooks.io/complete-python-web/content/section3/mongodb.html).

## Run Mongo
Start the server in the console (rather than in the background).
```
sudo mongod
```
In the second console, run the interactive console to interact with `mongod` server.
```
mongo
```
There's some output.  
Show databases.
```
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
```

## Basic Commands
Now, we can tell `mongo` to use a specific db, or to create a new one with the command `use <db>`.  
But it'll create the database, when you records the first data in it.
Create a new db, `fullstack`.
```
> use fullstack
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
```
Then, we can see the collections, which hold data, in our database. Because we have just created this database, they will be empty (no input).
```
> show collections
```
We can insert data into a non-existing collection. Accepts JSONs.
It'll also create the database.
```
> db.students.insert({"name": "Vassily", "mark": 99})
WriteResult({ "nInserted" : 1 })
> show collections
students
> show database
admin      0.000GB
config     0.000GB
fullstack  0.000GB
local      0.000GB
```
Check what's in there.
```
> db.students.find({})
{ "_id" : ObjectId("5b1304d4ef5289220c1d5442"), "name" : "Vassily", "mark" : 99 }
> db.students.find({"mark": 13})
> db.students.find({"mark": 99})
{ "_id" : ObjectId("5b1304d4ef5289220c1d5442"), "name" : "Vassily", "mark" : 99 }
```
Can insert different data type.
```
> db.students.insert({"item": "chair", "price": 999, "age": 23})
WriteResult({ "nInserted" : 1 })
> db.students.find({})
{ "_id" : ObjectId("5b1304d4ef5289220c1d5442"), "name" : "Vassily", "mark" : 99 }
{ "_id" : ObjectId("5b1305f70a0fe1d587b209be"), "item" : "chair", "price" : 999, "age" : 23 }
```
Now, you can remove the data.
```
> db.students.remove({"name": "Vassily"})
WriteResult({ "nRemoved" : 1 })
```

NEXT UP:
* [Terminal Blog - Uses Mongo and pymongo](004_terminal_blog_mongo_pymongo.md)
