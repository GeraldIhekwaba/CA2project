from flask import Flask,render_template

app = Flask(__name__)

# @app.route("/")
# def gerald():
#     return "<h1>Gerald is learning fast!</h1>"

# @app.route("/about")
# def about_page():
#     return "<p>Welcome to the about page</p>"

# @app.route("/about/<username>")
# def about_page_user (username):
#     return f"<p>Welcome to the about page of {username}</p>"

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html') 

@app.route("/market")
def market_pag():
    return  render_template('market.html')