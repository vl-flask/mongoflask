import pymongo

from database import Database
from models.post import Post

Database.initialize()
# post = Post.from_mongo('6a22009768e848eab580619a9ed75604')
# # Second variant
post = Post.from_blog("123")
print(post)

# post = Post(blog_id="123",
#             title="Another post",
#             content="Some sample content",
#             author="Vassily")
#
# post.save_to_mongo()

# post = Post("Post1 title", "Post1 content", "Post1 author")
# post2 = Post("Post2 title", "Post2 content", "Post2 author")
#
#
# print(post.content)
# print(post2.content)