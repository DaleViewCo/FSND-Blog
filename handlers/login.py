from handlers.bloghandler import BlogHandler
from models.user import User


class Login(BlogHandler):

    def get(self):
        if self.user:
            self.redirect('/blog')

        self.render('login.html', msg="")

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')

        u = User.login(username, password)
        if u:
            self.login(u)
            self.redirect('/blog')
        else:
            msg = 'Invalid login'
            self.render('login.html', msg=msg)
