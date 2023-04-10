from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)



class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Float(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)

    def __repr__(self):
        return f'Item {self.name}'

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
    items = Item.query.all()
    return  render_template('market.html',items=items)