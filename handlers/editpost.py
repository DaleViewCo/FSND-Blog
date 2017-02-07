from handlers.bloghandler import BlogHandler
import main
import json


class EditPost(BlogHandler):

    def get(self, url):
        if not self.user:
            self.redirect("/login")
            return

        post_id = url.replace("/edit",  "")

        if not self.is_valid_post(post_id):
            self.redirect('/blog')
            return

        post = self.get_post(post_id)

        if not self.is_author(post):
            self.redirect('/blog')
            return

        self.render("edit.html", p=post)

    def post(self, url):
        if not self.user:
            self.redirect("/login")
            return

        data = main.json_loads_byteified(self.request.body)
        post_id = data['pid']

        if not self.is_valid_post(post_id):
            self.redirect('/blog')
            return

        post = self.get_post(post_id)

        if not self.is_author(post):
            self.redirect('/blog')
            return

        post.content = data['post']
        post.subject = data['subject']
        post.put()

        result = {}
        result['post_id'] = post_id
        response_data = json.dumps(result)
        self.response.out.write(response_data)
