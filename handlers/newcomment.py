from handlers.bloghandler import BlogHandler
import main
import json

from models.comment import Comment


class NewComment(BlogHandler):

    def get(self):
        pass

    def post(self):
        data = main.json_loads_byteified(self.request.body)
        post_id = data['pid']
        comment_text = data['comment']
        user_id = str(self.read_secure_cookie('user_id'))

        if not self.user:
            self.redirect('/login')
            return

        if not self.is_valid_post(post_id):
            self.redirect('/blog')
            return

        post = self.get_post(post_id)

        commentdb = Comment(
            author_id=user_id,
            comment=comment_text,
            post_id=str(post_id)
        )

        comment_key = commentdb.put()
        post.comments.append(str(comment_key.id()))
        post.put()

        result = {}
        result['data'] = (main.render_str
                          ("comment.html",
                           comment=commentdb,
                           is_comment_author=True,
                           user_id=user_id))
        result['id'] = comment_key.id()

        response_data = json.dumps(result)
        self.response.out.write(response_data)
