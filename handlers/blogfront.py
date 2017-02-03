from models.post import Post
from handlers.bloghandler import BlogHandler


class BlogFront(BlogHandler):

    def get(self):
        if not self.user:
            self.redirect("/login")

        # get all posts in reverse order of creation

        posts = Post.all().order('-created')
        username = self.read_secure_cookie('user_name')
        self.render(
            'front.html', username=username, posts=posts)
