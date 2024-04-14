from app import app

from flask import render_template
from datetime import datetime

@app.template_filter("clean_date")
def clean_date(dt):
    return dt.strftime("%d %b %Y")

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/jinja")
def jinja():

    my_name = "Erick"

    age = 30

    langs = ["Python", "JavaScript", "Bash", "C"]

    friends = {
        "Mack": 33,
        "Mumo": 31,
        "Victor": 38,
        "Msanii": 39
    }

    colors = ("Red", "Grey", "Yellow")

    cool = True

    class GitRemote:
        def __init__(self, name, description, url):
            self.name = name
            self.description = description
            self.url = url
        def pull(self):
            return f"Pulling repo {self.name}"

        def clone(self):
            return f"Cloning into {self.url}"
    my_remote = GitRemote(
        name="Learning Flask",
        description="I'm learning flask as I build.",
        url="https://github.com/awinooliyo/learning-flask.git"
    )


    date = datetime.utcnow()

    my_html = "<h1>THIS IS SOME HTML</h1>"
    
    suspiscious = "<script>alert('YOU GOT HACKED!')</script>"
    
    def repeat(x, qty):
        return x * qty

    
    return render_template(
        "public/jinja.html", my_name=my_name, age=age,
        langs=langs, friends=friends,
        colors=colors, cool=cool, GitRemote=GitRemote,
        repeat=repeat, my_remote=my_remote, my_html=my_html, date=date,
        suspiscious=suspiscious
    )

@app.route("/about")
def about():
    return render_template("public/about.html")