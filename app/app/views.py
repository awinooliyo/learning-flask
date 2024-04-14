from app import app

@app.route("/")
def home():
    return "Hello! this is the main page <h1>Hello</h1>"

@app.route("/about")
def about():
    return "<h1 style='color:red'>Who we Are, Really?</h1>"
