import main
import json
from handlers.bloghandler import BlogHandler


class Like(BlogHandler):

    def get(self):
        pass

    def post(self):
        data = main.json_loads_byteified(self.request.body)

        post_id = data['pid']
        user_id = str(self.read_secure_cookie('user_id'))

        post = self.get_post(post_id)

        if not self.user:
            self.redirect('/login')
            return

        if not post:
            self.redirect('/blog')

        if self.is_author(post):
            return

        liked_by_authors = post.likes_list

        if user_id in liked_by_authors:
            result = {}
            result['data'] = post.likes
            response_data = json.dumps(result)
        else:
            liked_by_authors.append(user_id)
            post.likes_list = liked_by_authors
            post.likes = post.likes + 1
            post.put()
            result = {}
            result['data'] = post.likes
            response_data = json.dumps(result)

        self.response.out.write(response_data)
