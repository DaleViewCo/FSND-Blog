import main
from google.appengine.ext import db
import logging
from models.comment import Comment
import json


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
        return main.render_str("post.html", p=self, isPermaLink=False)

    def render_without_subject_link(self):
        self._render_text = self.content.replace('\n', '<br>')
        comment_html = ''
        logging.info("------Self Comments")
        logging.info(self.comments)
        for cid in self.comments:
            key = db.Key.from_path(
                'Comment', int(cid), parent=main.blog_key())
            comment_html += Comment.render(db.get(key))

        return main.render_str("post.html", p=self,
                               comment_html=comment_html,
                               isPermaLink=True)
