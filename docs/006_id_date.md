# Provide Default Values (ID and Date) and Test the Functions

# Provide the Default Id
If we already have an id, let's use it; otherwise let's generate it using `uuid` library.  
```python
import uuid

class Post(object):
    def __init__(self, blog_id, title, content, author, date, id=None):
        # [...]
        # There are several ways to generate uuids.
        # uuid.uuid4() means random id
        # hex gives a 32-char hexadecimal strings
        self.id = uuid.uuid4().hex
        # [...]
```
But let's use it only if there's no original ID in the json. And let's provide the default value of `None`.
```python
class Post(object):
    def __init__(self, blog_id, title, content, author, date, id=None):
        # [...]
        self.id = uuid.uuid4().hex if id is None else id
        # [...]
```

# Provide the Created Date
Import the `datetime` library, and use `datetime.datetime.utcnow()` as the default value.
```python
import datetime
...
class Post(object):
    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow(), id=None):
        # [...]
        self.created_date = date
        # [...]
```
This is how we can initialize a post.
```python
post = Post(blog_id="123", title="a title", content="some content", author="Vassily", id="1345")
```

## Verify that Post Methods Really Work
Initialize database object.  
Create a post and save it to the db.
```python
from database import Database
from models.post import Post

Database.initialize()

post = Post(blog_id="123",
            title="Another post",
            content="Some sample content",
            author="Vassily")
post.save_to_mongo()
```
Check using the mongo shell
```
> use fullstack
switched to db fullstack
> db.posts.find({})
{ "_id" : ObjectId("5b199ee05483f52ed0858695"), "id" : "6a22009768e848eab580619a9ed75604", "blog_id" : "123", "author" : "Vassily", "content" : "Some sample content", "title" : "Another post", "created_date" : ISODate("2018-06-07T21:08:48.630Z") }
```
Next make sure you can find it using the `id` from above.
```python
from database import Database
from models.post import Post
Database.initialize()
post = Post.from_mongo('6a22009768e848eab580619a9ed75604')
# # Second variant
# post = Post.from_blog("123")
print(post)
```
