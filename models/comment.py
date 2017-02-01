import main
from google.appengine.ext import db
import logging


class Comment(db.Model):
    author_id = db.StringProperty(required=True)
    comment = db.StringProperty(required=True)

    def render(self, user_id):
        return main.render_str("comment.html", comment=self, user_id=user_id)
