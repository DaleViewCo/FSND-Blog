import main
from google.appengine.ext import db
from google.appengine.ext.db import KindError
import logging


class Comment(db.Model):
    author = db.StringProperty(required=True)
    comment = db.StringProperty(required=True)
    # created = db.TextProperty(required=True)
    # last_modified = db.DateTimeProperty(auto_now=True)

    def render(self):
        return main.render_str("comment.html", comment=self)

    # def render_comments(self, comment_id):
    #     try:
    #         commentdb = db.GqlQuery(
    #             "SELECT * FROM Comment WHERE comment_id = %s", comment_id)
    #         return main.render_str("comment.html", comment_list=commentdb)
    #     except KindError:
    #         logging.info('No entity yet')
