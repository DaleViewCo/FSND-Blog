from handlers.bloghandler import BlogHandler
from google.appengine.ext import db
import main
import json
import logging


class EditPost(BlogHandler):

    def get(self, url):
        post_id = url.replace("/edit",  "")
        key = db.Key.from_path('Post', int(post_id), parent=main.blog_key())
        post = db.get(key)
        self.render("edit.html", p=post)

    def post(self, url):
        post_id = url.replace("/edit",  "")
        logging.info("In EDIT POST")
        data = main.json_loads_byteified(self.request.body)
        logging.info(data)
        key = db.Key.from_path('Post', int(post_id), parent=main.blog_key())
        post = db.get(key)

        post.content = data['post']
        post.put()

        result = {}
        result['post_id'] = post_id
        response_data = json.dumps(result)
        self.response.out.write(response_data)
