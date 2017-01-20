from handlers.bloghandler import BlogHandler
from google.appengine.ext import db
import main
import json
import logging


class PostPage(BlogHandler):

    def get(self, post_id):
        logging.info("GET CALLED")
        key = db.Key.from_path('Post', int(post_id), parent=main.blog_key())
        post = db.get(key)
        home = 'front.html'
        post_id = post.key().id()

        if not self.post:
            self.error(404)
            return

        self.render(
            "permalink.html", post=post, home=home,
            post_id=post_id)

    def post(self, data):
        # logging.info("POST method called in postpage")
        # logging.info(self.request.get().body())
        data = json.loads(self.request.body)
        logging.info(data)
        # self.response.out.write(
        #     json.dumps(({'comment_content': "Hello World"})))
        # self.render(
        #     "permalink.html", post=post)
