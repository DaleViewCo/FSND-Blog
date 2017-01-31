import main
from google.appengine.ext import db
from google.appengine.ext.db import KindError
import logging


class Comment(db.Model):
    author = db.StringProperty(required=True)
    comment = db.StringProperty(required=True)

    def render(self):
        return main.render_str("comment.html", comment=self)
