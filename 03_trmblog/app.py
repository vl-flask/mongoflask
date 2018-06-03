from models.post import Post
post1 = Post("Post 1 title", "Post 1 content", "Post 1 author")
post2 = Post("Post 2 title", "Post 2 content", "Post 2 author")
print(post1.content)
print(post2.content)

# Old version. Removed when created Post()
# import pymongo
#
# uri = "mongodb://127.0.0.1:27017"
# client = pymongo.MongoClient(uri)
# database = client['fullstack']
# collection = database['students']
# students = [student['mark'] for student in collection.find({}) if student['mark'] == 99.0]
# print(students)

# students = collection.find({})

# The one below is incorrect
# print(students)
# The results will be:
# (trm) vl@mfla:~/Learn/fl/01-compl-8/03_trmblog$ python app.py
# <pymongo.cursor.Cursor object at 0x7fe679458518>
# The correct one is below

# for student in students:
#     print(student)
