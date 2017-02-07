import webapp2
from google.appengine.ext import db
import main
from models.user import User


class BlogHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        params['user'] = self.user
        return main.render_str(template, **params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def set_secure_cookie(self, name, val):
        cookie_val = main.make_secure_val(val)
        self.response.headers.add_header(
            'Set-Cookie',
            '%s=%s; Path=/' % (name, cookie_val))

    def read_secure_cookie(self, name):
        cookie_val = self.request.cookies.get(name)
        return cookie_val and main.check_secure_val(cookie_val)

    def login(self, user):
        self.set_secure_cookie('user_id', str(user.key().id()))
        self.set_secure_cookie('user_name', str(user.name))

    def logout(self):
        self.response.headers.add_header('Set-Cookie', 'user_id=; Path=/')

    def is_author(self, entry):
        return self.user and self.read_secure_cookie('user_id') == str(
            entry.author_id)

    def is_valid_post(self, post_id):
        post = self.get_post(post_id)
        if post:
            return True
        else:
            return False

    def is_valid_comment(self, comment_id):
        comment = self.get_comment(comment_id)
        if comment:
            return True
        else:
            return False

    def get_post(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=main.blog_key())
        post = db.get(key)
        return post

    def get_comment(self, comment_id):
        comment_key = db.Key.from_path(
            'Comment', int(comment_id))
        commentdb = db.get(comment_key)
        return commentdb

    def initialize(self, *a, **kw):
        webapp2.RequestHandler.initialize(self, *a, **kw)
        uid = self.read_secure_cookie('user_id')
        self.user = uid and User.by_id(int(uid))
