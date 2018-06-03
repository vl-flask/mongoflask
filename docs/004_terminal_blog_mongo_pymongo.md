# Start Terminal Blog

## Set Up a New Project
Create a new proj, a new venv, `app.py`, and a new req's file.
```
mkdir 03_trmblog
touch 03_trmblog/app.py
touch 03_trmblog/reqs.txt
mkvirtualenv trm
pip install pymongo==3.6.1
```
In `app.py`, import `pymongo`, specify the MongoDB instance, initialize the MDB client (accesses yr DB's), specify the database.
```
import pymongo

uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['fullstack']
collection = database['students']
students = collection.find({})
```
Now, we can try to print the students `print(students)`, but it'll only return a cursor object.
```
(trm) vl@mfla:~/Learn/fl/01-compl-8/03_trmblog$ python app.py
<pymongo.cursor.Cursor object at 0x7fe679458518>
```
The correct way will be to loop over the student items.
```
for s in students:
    print(s)
```
The result w. be:
```
(trm) vl@mfla:~/Learn/fl/01-compl-8/03_trmblog$ python app.py
{'_id': ObjectId('5b1304d4ef5289220c1d5442'), 'name': 'Vassily', 'mark': 99.0}
```
But it's a poor way. If we nd to list the students, then we do something like that:
```python
students = collection.find({})
student_list = []
for s in students:
  student_list.append(s)
```
We can do better with list comprehensions.
```python
[student for student in collection.find({})]
```
We can improve it.
```python
students = [student['mark'] for student in collection.find({}) if student['mark'] == 100]
print(students)
```
Run here. The will be empty though, as no student has grade 100.  
Change the mark to 99.0. There'll be some.
```
(trm) vl@mfla:~/Learn/fl/01-compl-8/03_trmblog$ python app.py
[]
(trm) vl@mfla:~/Learn/fl/01-compl-8/03_trmblog$ python app.py
[99.0]
```

NEXT UP:
* [Terminal Blog Intro To OOP](005_tblog_intro_oop.md)
