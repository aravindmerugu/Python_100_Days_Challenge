import requests
from flask import Flask, render_template
from post import Post

app = Flask(__name__)

post_list = []

link = 'https://jsonkeeper.com/b/JE6F'
response = requests.get(link)
blog_posts = response.json()
print(blog_posts)

for post_obj in blog_posts:
    obj = Post(post_obj["id"],post_obj["title"],post_obj["subtitle"],post_obj["body"])
    post_list.append(obj)

@app.route('/')
def home():
    return render_template("index.html", posts=blog_posts)


@app.route('/blog<int:id>')
def blog_post(id):
    ind = id-1
    display_post =  post_list[ind]
    print(display_post)
    return render_template("post.html", postobj=display_post)

if __name__ == "__main__":
    app.run(debug=True)
