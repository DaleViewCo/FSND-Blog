from models.post import Post
from handlers.bloghandler import BlogHandler


class BlogFront(BlogHandler):

    def get(self):
        posts = Post.all().order('-created')
        username = self.read_secure_cookie('user_name')
        self.render(
            'front.html', username=username, posts=posts)
