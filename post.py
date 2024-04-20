import requests

class Post:
    def __init__(self):
        self.response = requests.get(url="https://api.npoint.io/1053241c471c8af78b80").json()

    def blog_title(self, blog_id):
        return self.response[blog_id]["title"]

    def blog_subtitle(self, blog_id):
        return self.response[blog_id]["subtitle"]

    def blog_body(self, blog_id):
        return self.response[blog_id]["body"]

    def blog_author(self, blog_id):
        return self.response[blog_id]["author"]

    def blog_date(self, blog_id):
        return self.response[blog_id]["date"]

    def blog_image(self, blog_id):
        return self.response[blog_id]["image"]