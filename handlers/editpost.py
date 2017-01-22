from handlers.bloghandler import BlogHandler
from models.comment import Comment
from google.appengine.ext import db
import main
import json
import logging


class EditPost(BlogHandler):

    def get(self, post_id):
        post_id = self.read_secure_cookie('post_id')
        key = db.Key.from_path('Post', int(post_id), parent=main.blog_key())
        post = db.get(key)
        self.render("edit.html", p=post)
