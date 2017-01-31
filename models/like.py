from google.appengine.ext import db


class Like(db.Model):
    author_id = db.StringProperty(required=True)
