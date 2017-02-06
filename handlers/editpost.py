from handlers.bloghandler import BlogHandler
from google.appengine.ext import db
import main
import json


class EditPost(BlogHandler):

    def get(self, url):
        if not self.user:
            self.redirect("/login")
            return

        post_id = url.replace("/edit",  "")
        post = self.is_valid_post(post_id)

        if not self.is_author(post):
            self.redirect('/blog')
            return

        self.render("edit.html", p=post)

    def post(self, url):
        if not self.user:
            self.redirect("/login")
            return

        # get post id from the url
        post_id = url.replace("/edit",  "")

        data = main.json_loads_byteified(self.request.body)
        post = self.is_valid_post(post_id)

        if not self.is_author(post):
            self.redirect('/blog')
            return

        post.content = data['post']
        post.subject = data['subject']
        post.put()

        result = {}
        result['post_id'] = post_id
        response_data = json.dumps(result)
        self.response.out.write(response_data)
