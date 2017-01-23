from handlers.bloghandler import BlogHandler
from models.comment import Comment
from google.appengine.ext import db
import main
import json


class PostPage(BlogHandler):

    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=main.blog_key())
        post = db.get(key)
        home = 'front.html'
        post_id = post.key().id()

        if not self.post:
            self.error(404)
            return

        is_author = post.author_id == self.read_secure_cookie('user_id')

        self.render(
            "permalink.html", post=post, home=home,
            post_id=post_id, is_author=is_author)

    def post(self, data):
        if self.user:
            data = main.json_loads_byteified(self.request.body)
            post_id = data['pid']
            comment_text = data['comment']

            commentdb = Comment(
                author=self.read_secure_cookie('user_name'),
                comment=comment_text,
            )
            commentdb.put()

            key = db.Key.from_path(
                'Post', int(post_id), parent=main.blog_key())
            post = db.get(key)
            post.comments.append(comment_text)
            post.put()

            result = {}
            result['data'] = (main.render_str
                              ("comment.html",
                               comment=commentdb))

            response_data = json.dumps(result)
            self.response.out.write(response_data)
