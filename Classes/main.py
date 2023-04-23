from user import User
from post import Post

#Classes and Method example in Python
user = User(user_email="aa", password="aa",name="Kash",current_job_title="aa")
user.get_user_info()

post = Post(message="First Post", author="Prakash")
post.get_post_info()