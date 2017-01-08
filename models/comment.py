import main
from google.appengine.ext import db


class Comment(db.Model):
    author = db.StringProperty(required=True)
    comment = db.StringProperty(required=True)
    created = db.TextProperty(required=True)
    last_modified = db.DateTimeProperty(auto_now=True)

    def render(self):
        self._render_text = self.content.replace('\n', '<br>')
        return main.render_str("comment.html", comment=self)
