from handlers.bloghandler import BlogHandler
from google.appengine.ext import db
import main


class PostPage(BlogHandler):

    def get(self, post_id):
        if not self.user:
            self.redirect("/login")
            return

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

    def post(self):
        pass
