from models.post import Post
from handlers.bloghandler import BlogHandler
import logging


class BlogFront(BlogHandler):

    def get(self):
        if not self.user:
            self.redirect("/login")

        logging.info("IN BLOG FRONT")
        posts = Post.all().order('-created')
        logging.info(posts)
        for p in posts:
            logging.info(p.content)
        username = self.read_secure_cookie('user_name')
        self.render(
            'front.html', username=username, posts=posts)
