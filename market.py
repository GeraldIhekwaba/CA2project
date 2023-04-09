from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABSE_URI'] = 'sqlite://market.db'
db = SQLAlchemy(app)
db.init_app(app)


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Float(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)

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