import main
from models.comment import Comment
from google.appengine.ext import db


class Post(db.Model):
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    author = db.TextProperty(required=True)
    likes = db.IntegerProperty(required=True)
    comments = db.ListProperty(str, required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)
    rendered_comments = ''

    def render(self):
        comment_db = Comment.all()
        if comment_db:
            for comment in comment_db:
                if comment.key().id() in self.comments:
                    self.rendered_comments = (self.rendered_comments +
                                              main.render_str("comment.html",
                                                              comment=comment))

        self._render_text = self.content.replace('\n', '<br>')
        return main.render_str("post.html", p=self)
