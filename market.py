from flask import Flask

app = Flask(__name__)

@app.route("/")
def gerald():
    return "<p>Gerald is learning</p>"