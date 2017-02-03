from handlers.bloghandler import BlogHandler
from models.comment import Comment
from google.appengine.ext import db
import main
import json


class PostPage(BlogHandler):

    def get(self, post_id):
        if not self.user:
            self.redirect("/login")

        key = db.Key.from_path('Post', int(post_id), parent=main.blog_key())
        post = db.get(key)

        '''
        when the existing post is deleted, hitting back/copy pasting url with
        post id should not go to blank page
        '''
        if not post:
            self.redirect('/blog')
            return

        home = 'front.html'
        post_id = post.key().id()

        if not self.post:
            self.error(404)
            return

        user_id = self.read_secure_cookie('user_id')
        is_author = post.author_id == user_id

        comment_ids = post.comments
        comment_db_list = []

        # check if Post has associated comments

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

        # get type of operation

        post_type = data['type']

        user_id = str(self.read_secure_cookie('user_id'))

        if self.user and post_type == "DeletePost":

            # Delete Post and associated comments

            post_id = data['pid']
            key = db.Key.from_path(
                'Post', int(post_id), parent=main.blog_key())
            post = db.get(key)

            for cid in post.comments:
                comment_key = db.Key.from_path(
                    'Comment', int(cid))
                commentdb = db.get(comment_key)
                commentdb.delete()

            post.delete()
            result = {}
            result['data'] = ""
            response_data = json.dumps(result)
            self.response.out.write(response_data)

        elif self.user and post_type == "NewComment":

            # create new Comment and associate with the Post

            post_id = data['pid']
            key = db.Key.from_path(
                'Post', int(post_id), parent=main.blog_key())
            post = db.get(key)

            comment_text = data['comment']
            commentdb = Comment(
                author_id=user_id,
                comment=comment_text,
                post_id=str(post_id)
            )
            comment_key = commentdb.put()
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

            # update comment text in Comment

            comment_text = data['edited-comment']
            comment_id = data['comment-id']

            comment_key = db.Key.from_path(
                'Comment', int(comment_id))
            commentdb = db.get(comment_key)
            commentdb.comment = comment_text
            commentdb.put()
            result = {}
            result['data'] = comment_text
            response_data = json.dumps(result)
            self.response.out.write(response_data)

        elif self.user and post_type == "DeleteComment":

            # delete from Comment and remove association from Post

            post_id = data['pid']
            comment_id = data['comment-id']

            comment_key = db.Key.from_path(
                'Comment', int(comment_id))
            commentdb = db.get(comment_key)
            commentdb.delete()

            key = db.Key.from_path(
                'Post', int(post_id), parent=main.blog_key())
            post = db.get(key)
            post.comments.remove(str(comment_id))
            post.put()

            result = {}
            result['data'] = "deleted"
            response_data = json.dumps(result)
            self.response.out.write(response_data)

        else:
            if not self.user:
                return

            # must have hit the Like button (only shown when user != author)

            post_id = data['pid']
            key = db.Key.from_path(
                'Post', int(post_id), parent=main.blog_key())
            post = db.get(key)

            # only increment like count if not liked yet by the user

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
