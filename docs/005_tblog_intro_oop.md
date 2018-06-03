# Terminal Blog - Intro to OOP

## Create the First Model
Create a new package named `models` and add a file for the `Post` model.
```
mkdir models
cd models
touch __init__.py post.py
```
Create the initial Post class (`models/post.py`).
```python
class Post(object):
    def __init__(self):
        self.title = "This is my title"
        self.content = "This is some content"
        self.author = "Jose"
```
Remove everything from `app.py`, create two Post objects, make it print the content.
```python
from models.post import Post
post = Post()
post2 = Post()
print(post.content)
print(post2.content)
```
Run the script.
```
$ python app.py
This is some content
This is some content
```
But we can change properties in our program.
```python
# [...]
post2.content = "Some different content"
# [...]
```
Now we can run it...
```
$ python app.py
This is some content
Some different content
```
But we still only initialize posts with those original hardcoded values.  
To improve it, we do the following (`models/post.py`).
```python
class Post(self, title, content, author):
    def __init__(self):
        self.title = title
        self.content = content
        self.author = author
```
Initialize the objects in `app.py`.
```
post1 = Post("Post 1 title", "Post 1 content", "Post 1 author")
post2 = Post("Post 2 title", "Post 2 content", "Post 2 author")
print(post1.content)
print(post2.content)
```
Run the thing.
```
$ python app.py
Post 1 content
Post 2 content
```

## Make the Post nice
Add the post id and the blog id to the model (`models/post.py`).   Also provide the methods for saving the post to the db.
```python
class Post(object):
    def __init__(self, blog_id, title, content, author, id):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = date
        self.id = id
    # We can say the post provides a method for saving it to the db
    def save_to_mongo(self):
        pass
```
Create a method that creates a JSON representation of itself.
```python
class Post(object):
    # [...]
    def json(self):
        return {
            'id': self.id,
            'blog_id': self.blog_id
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.created_date
        }
```
Now, everything we have to do to save the data to db is to add this json to it. Simplified thing:
```python
class Post(object):
    # [...]
    def save_to_mongo(self):
        Database.insert(
                collection = 'posts',
                data = self.json
        )
    # [...]
```
Okay, we just wrote `Database.insert...`, so we need to create this thing.  
Create a python file for it outside the package.
```
touch database.py
```
