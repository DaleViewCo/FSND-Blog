from handlers.bloghandler import BlogHandler
from google.appengine.ext import db
import main
import json


class PostPage(BlogHandler):

    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=main.blog_key())
        post = db.get(key)
        home = 'front.html'

        if not post:
            self.error(404)
            return

        self.render("permalink.html", post=post, home=home)

    def post(self):
        data = json.loads(self.request.body)
        self.response.out.write(
            json.dumps(({'comment_content': "Hello World"})))
