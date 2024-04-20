from flask import Flask, render_template
from post import Post

app = Flask(__name__)

post = Post()


@app.route("/")
def get_all_post():
    return render_template('index.html', posts=post.response)


@app.route("/home")
def home():
    return render_template('index.html', posts=post.response)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/post/<int:blog_id>")
def show_post(blog_id):
    return render_template("post.html",
                           title=post.blog_title(blog_id),
                           subtitle=post.blog_subtitle(blog_id),
                           author=post.blog_author(blog_id),
                           date=post.blog_date(blog_id),
                           image=post.blog_image(blog_id),
                           body=post.blog_body(blog_id))


if __name__ == "__main__":
    app.run(debug=True)
