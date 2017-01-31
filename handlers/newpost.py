from handlers.bloghandler import BlogHandler
from models.post import Post
import main


class NewPost(BlogHandler):

    def get(self):
        if self.user:
            self.render("newpost.html")
        else:
            self.redirect("/login")

    def post(self):
        if not self.user:
            self.redirect('/blog')

        subject = self.request.get('subject')
        content = self.request.get('content')
        author = self.read_secure_cookie('user_name')
        author_id = self.read_secure_cookie('user_id')
        likes = 0
        comment_list = []
        likes_list = []

        if subject and content:
            p = Post(
                parent=main.blog_key(),
                subject=subject,
                author=author,
                author_id=author_id,
                likes=likes,
                likes_list=likes_list,
                content=content,
                comments=comment_list
            )
            p.put()
            self.redirect('/blog/%s' % str(p.key().id()))
        else:
            error = "Missing Subject/Content!"
            self.render(
                "newpost.html", subject=subject, content=content, error=error)
