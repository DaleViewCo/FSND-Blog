from handlers.bloghandler import BlogHandler
from models.comment import Comment
from google.appengine.ext import db
import main
import json
import logging


class PostPage(BlogHandler):

    def get(self, post_id):
        if not self.user:
            self.redirect("/login")

        key = db.Key.from_path('Post', int(post_id), parent=main.blog_key())
        post = db.get(key)
        home = 'front.html'
        post_id = post.key().id()

        if not self.post:
            self.error(404)
            return

        user_id = self.read_secure_cookie('user_id')
        is_author = post.author_id == user_id

        comment_ids = post.comments
        comment_db_list = []

        for k in comment_ids:
            key = db.Key.from_path(
                'Comment', int(k))
            comment = db.get(key)
            if comment is None:
                pass
            else:
                comment_db_list.append(comment)

        self.render(
            "permalink.html", post=post, home=home,
            post_id=post_id, is_author=is_author,
            comment_db_list=comment_db_list, user_id=user_id)

    def post(self, data):
        data = main.json_loads_byteified(self.request.body)
        post_type = data['type']

        user_id = str(self.read_secure_cookie('user_id'))

        if self.user and post_type == "NewComment":
            comment_text = data['comment']
            commentdb = Comment(
                author_id=user_id,
                comment=comment_text,
            )
            comment_key = commentdb.put()

            post_id = data['pid']
            key = db.Key.from_path(
                'Post', int(post_id), parent=main.blog_key())
            post = db.get(key)

            post.comments.append(str(comment_key.id()))
            post.put()
            is_comment_author = user_id == commentdb.author_id

            result = {}
            result['data'] = (main.render_str
                              ("comment.html",
                               comment=commentdb,
                               is_comment_author=is_comment_author,
                               user_id=user_id))
            result['id'] = comment_key.id()

            response_data = json.dumps(result)
            self.response.out.write(response_data)

        elif self.user and post_type == "EditComment":
            comment_text = data['edited-comment']
            comment_id = data['comment-id']
            logging.info(comment_text)

            comment_key = db.Key.from_path(
                'Comment', int(comment_id))
            commentdb = db.get(comment_key)
            commentdb.comment = comment_text
            commentdb.put()
            result = {}
            result['data'] = comment_text
            response_data = json.dumps(result)
            self.response.out.write(response_data)

        else:
            post_id = data['pid']
            key = db.Key.from_path(
                'Post', int(post_id), parent=main.blog_key())
            post = db.get(key)

            if post_type == "Like":
                liked_by_authors = post.likes_list
                if user_id in liked_by_authors:
                    result = {}
                    result['data'] = post.likes
                    response_data = json.dumps(result)
                else:
                    liked_by_authors.append(user_id)
                    post.likes_list = liked_by_authors
                    post.likes = post.likes + 1
                    post.put()
                    result = {}
                    result['data'] = post.likes
                    response_data = json.dumps(result)

            self.response.out.write(response_data)
