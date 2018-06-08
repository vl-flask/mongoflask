import uuid
import datetime

from database import Database

class Post(object):

    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow(), id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = date
        # There are several ways to generate uuids.
        # uuid.uuid4() means random id
        # hex gives a 32-char hexadecimal strings
        self.id = uuid.uuid4().hex if id is None else id

        # post = Post(blog_id="123", title="a title", content="some content", author="Vassily", id="1345", date=da)

    def save_to_mongo(self):
        Database.insert(collection='posts',
                        data=self.json())

    def json(self):
        return {
            'id': self.id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.created_date
        }

    @staticmethod
    def from_mongo(id):
        return Database.find_one(collection='posts', query={'id': id})

    @staticmethod
    def from_blog(id):
        blog_posts = Database.find(collection='posts', query={'blog_id': id})
        return [post for post in blog_posts]