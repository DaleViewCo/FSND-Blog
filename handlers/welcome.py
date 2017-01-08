from handlers.bloghandler import BlogHandler
import main


class Welcome(BlogHandler):

    def get(self):
        username = self.request.get('username')
        if main.valid_username(username):
            self.render('welcome.html', username=username)
        else:
            self.redirect('/signup')
