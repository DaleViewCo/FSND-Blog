from handlers.bloghandler import BlogHandler
from google.appengine.ext import db
import main


class PostPage(BlogHandler):

    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=main.blog_key())
        post = db.get(key)
        home = 'front.html'

        if not post:
            self.error(404)
            return

        self.render("permalink.html", post=post, home=home)
