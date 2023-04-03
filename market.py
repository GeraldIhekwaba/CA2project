from flask import Flask

app = Flask(__name__)

@app.route("/")
def gerald():
    return "<h1>Gerald is learning fast!</h1>"

@app.route("/about")
def about_page():
    return "<p>Welcome to the about page</p>"