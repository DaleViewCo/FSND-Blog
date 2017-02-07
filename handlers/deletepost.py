from handlers.bloghandler import BlogHandler
import main
import json


class DeletePost(BlogHandler):

    def get(self):
        pass

    def post(self):
        data = main.json_loads_byteified(self.request.body)
        post_id = data['pid']

        if not self.user:
            self.redirect('/login')
            return

        if not self.is_valid_post(post_id):
            self.redirect('/blog')
            return

        post = self.get_post(post_id)

        if not self.is_author(post):
            self.redirect('/blog')
            return

        for cid in post.comments:
            comment = self.get_comment(cid)
            if comment:
                comment.delete()

        post.delete()
        result = {}
        result['data'] = ""
        response_data = json.dumps(result)
        self.response.out.write(response_data)
