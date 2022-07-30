from flask import Flask, jsonify, request

from models import db, connect_db, User, Seed, Poem
from Markov import MarkovMachine

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///flask_markov'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)


@app.get('/')
def homepage():
    """returns a basic greeting"""

    return "HELLO WORLD"


@app.get('/users')
def list_users():
    """returns all users in system
    
    returns JSON like:"""

    users = [user.serialize() for user in User.query.all()]

    return jsonify(users=users)


@app.get('/users/<int:user_id>')
def get_user(user_id):
    """returns data on one user"""

    user = User.query.get_or_404(user_id)

    return jsonify(user=user.serialize())


@app.get('/seeds')
def list_seeds():
    """returns all users in system
    
    returns JSON like:"""

    seeds = [seed.serialize() for seed in Seed.query.all()]

    return jsonify(seeds=seeds)


@app.post('/seeds')
def create_seed():
    data = request.json
    print(data)

    seed = Seed(
        id=data['id'],
        title=data['title'],
        text=data['text'],
        author=data['author'],
        submitted_by_user_id=1,
    )
    db.session.add(seed)
    db.session.commit()

    return jsonify(seed=seed.serialize())


@app.get('/seeds/<int:seed_id>')
def get_seed(seed_id):
    """returns data on one seed"""

    seed = Seed.query.get_or_404(seed_id)

    return jsonify(seed=seed.serialize())


@app.get('/seeds/<int:seed_id>/generate')
def generate_poem(seed_id):
    """returns string of poem generated with seed_id"""

    seed = Seed.query.get_or_404(seed_id)
    text_generator = MarkovMachine(seed.text)

    return text_generator.get_text()


@app.get('/poems')
def list_poems():
    """returns all users in system
    
    returns JSON like:"""

    poems = [poem.serialize() for poem in Poem.query.all()]

    return jsonify(poems=poems)


@app.post('/poems')
def create_poem():
    data = request.json

    poem = Poem(
        id=data['id'],
        seed_id= data['seed_id'],
        text=data['text'],
        submitted_by_user_id=1
    )
    db.session.add(poem)
    db.session.commit()

    return jsonify(poem=poem.serialize())


@app.get('/poems/<int:poem_id>')
def get_poem(poem_id):
    """returns data on one poem"""

    poem = Poem.query.get_or_404(poem_id)

    return jsonify(poem=poem.serialize())