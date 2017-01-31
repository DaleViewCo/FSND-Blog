import main
from google.appengine.ext import db


class Post(db.Model):
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    author = db.TextProperty(required=True)
    author_id = db.StringProperty(required=True)
    likes_list = db.ListProperty(str, required=True)
    comments = db.ListProperty(str, required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)
    likes = db.IntegerProperty(required=False)

    def render(self, with_comments):
        self._render_text = self.content.replace('\n', '<br>')
        return main.render_str("frontsummary.html", p=self)

    def renderWithLikeButton(self, is_author):
        self._render_text = self.content.replace('\n', '<br>')
        return main.render_str("post.html", p=self, is_author=is_author)
