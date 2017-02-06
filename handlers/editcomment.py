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

        post = self.get_post(post_id)
        comment = self.get_comment(comment_id)

        if not self.user:
            self.redirect('/login')
            return

        if not self.is_author(comment):
            self.error(404)
            return

        if not post or not comment:
            self.redirect('/blog')
            return

        comment.comment = comment_text
        comment.put()
        result = {}
        result['data'] = comment_text
        response_data = json.dumps(result)
        self.response.out.write(response_data)
