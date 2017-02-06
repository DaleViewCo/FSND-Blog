import main
import json
from handlers.bloghandler import BlogHandler


class DeleteComment(BlogHandler):

    def get(self):
        pass

    def post(self):
        data = main.json_loads_byteified(self.request.body)

        post_id = data['pid']
        comment_id = data['comment-id']

        post = self.get_post(post_id)
        comment = self.get_comment(comment_id)

        if not self.user:
            self.redirect('/login')
            return

        if not post or not comment:
            self.redirect('/blog')
            return

        if not self.is_author(comment):
            self.error(404)
            return

        comment.delete()
        post.comments.remove(str(comment_id))

        result = {}
        result['data'] = ""
        response_data = json.dumps(result)
        self.response.out.write(response_data)
