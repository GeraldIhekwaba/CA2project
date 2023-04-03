from flask import Flask

app = Flask(__name__)

@app.route("/")
def gerald():
    return "<h1>Gerald is learning fast!</h1>"
