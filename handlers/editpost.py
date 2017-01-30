from handlers.bloghandler import BlogHandler
from google.appengine.ext import db
import main
import json


class EditPost(BlogHandler):

    def get(self, url):
        post_id = url.replace("/edit",  "")
        key = db.Key.from_path('Post', int(post_id), parent=main.blog_key())
        post = db.get(key)
        self.render("edit.html", p=post)

    def post(self, url):
        post_id = url.replace("/edit",  "")
        data = main.json_loads_byteified(self.request.body)
        key = db.Key.from_path('Post', int(post_id), parent=main.blog_key())
        post = db.get(key)

        post.content = data['post']
        post.subject = data['subject']
        post.put()

        result = {}
        result['post_id'] = post_id
        response_data = json.dumps(result)
        self.response.out.write(response_data)
