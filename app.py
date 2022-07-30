from flask import Flask

from models import connect_db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///flask-markov'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

@app.get('/')
def homepage():
    """returns a basic greeting"""

    return "HELLO WORLD"
