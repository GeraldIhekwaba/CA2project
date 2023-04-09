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
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150} 
    ]
    return  render_template('market.html',items=items)