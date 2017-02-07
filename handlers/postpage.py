from handlers.bloghandler import BlogHandler
from google.appengine.ext import db


class PostPage(BlogHandler):

    def get(self, post_id):

        if not self.user:
            self.redirect("/login")
            return

        if not self.is_valid_post(post_id):
            self.redirect('/blog')
            return

        '''
        when the existing post is deleted, hitting back/copy pasting url with
        post id should not go to blank page
        '''

        post = self.get_post(post_id)
        home = 'front.html'

        user_id = self.read_secure_cookie('user_id')
        is_author = post.author_id == user_id

        comment_ids = post.comments
        comment_db_list = []

        # check if Post has associated comments

        for k in comment_ids:
            comment = self.get_comment(k)
            if comment:
                comment_db_list.append(comment)

        self.render(
            "permalink.html", post=post, home=home,
            post_id=post_id, is_author=is_author,
            comment_db_list=comment_db_list, user_id=user_id)

    def post(self):
        pass
