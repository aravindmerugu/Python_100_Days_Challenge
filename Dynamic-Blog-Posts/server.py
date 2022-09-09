from flask import Flask, render_template
import requests
import random
import datetime

app = Flask(__name__)


# random_number = random.randint(1,100)
# year = datetime.datetime.now().year


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<name>")
def name_route(name):
    parameters = {
        "name": name
    }
    gender_response = requests.get("https://api.genderize.io", params=parameters)
    age_response = requests.get("https://api.agify.io", params=parameters)
    print(gender_response.json()["gender"])
    print(age_response.json()["age"])
    return render_template("person.html", name=name, gender=gender_response.json()["gender"],
                           age=age_response.json()["age"])

@app.route("/blog<num>")
def blog(num):
    link = 'https://jsonkeeper.com/b/JE6F'
    response = requests.get(link)
    blog_posts = response.json()
    print(blog_posts)
    return render_template("blog.html", posts = blog_posts, num=num)


if __name__ == "__main__":
    app.run(debug=True)