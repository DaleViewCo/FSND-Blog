import main
import json
from handlers.bloghandler import BlogHandler


class EditComment(BlogHandler):

    def get(self):
        pass

    def post(self):
        data = main.json_loads_byteified(self.request.body)

        post_id = data['pid']
        comment_id = data['comment-id']
        comment_text = data['edited-comment']

        if not self.user:
            self.redirect('/login')
            return

        if not self.is_valid_post(post_id):
            self.redirect('/blog')
            return

        if not self.is_valid_comment(comment_id):
            self.redirect('/blog')
            return

        comment = self.get_comment(comment_id)

        if not self.is_author(comment):
            self.redirect('/blog')
            return

        comment.comment = comment_text
        comment.put()
        result = {}
        result['data'] = comment_text
        response_data = json.dumps(result)
        self.response.out.write(response_data)
