import main
from google.appengine.ext import db


class Post(db.Model):
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    author = db.TextProperty(required=True)
    likes = db.IntegerProperty(required=True)
    comments = db.ListProperty(str, required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)

    def render(self):
        self._render_text = self.content.replace('\n', '<br>')
        return main.render_str("post.html", p=self, isNotPermaLink=True)

    def render_without_subject_link(self):
        self._render_text = self.content.replace('\n', '<br>')
        return main.render_str("post.html", p=self, isNotPermaLink=False)
