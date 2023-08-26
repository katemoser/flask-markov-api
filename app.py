from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import os

from models import db, connect_db, User, Seed, Poem, HoroscopeSeed
from Markov import MarkovMachine

from poems.routes import poems
from horoscope_scraper import HoroScraper

app = Flask(__name__)
CORS(app)

app.register_blueprint(poems)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ['SECRET-KEY']
app.config['SQLALCHEMY_ECHO'] = True

# Setup admin page
admin = Admin(app)
admin.add_view(ModelView(Poem,db.session))

connect_db(app)



@app.get('/')
def homepage():
    """Returns a basic greeting."""

    return "HELLO WORLD"


@app.get('/users')
def list_users():
    """returns all info on all users in system

    returns JSON like: {users: [user, ...] }
    with user like: {
            "first_name": "Kate",
			"id": 1,
			"last_name": "Moser",
			"liked_poems": [poem, ...],
            "submitted_poems": [poem, ...]
            "submitted_seeds": [ seed, ...] }
        with seed like:
        {
            "author": "Kate",
			"id": 123,
			"poems_seeded": [ poem, ...],
			"submitted_at": "Sat, 30 Jul 2022 15:45:37 GMT",
			"submitted_by_user_id": 1,
			"text": "This seed is the best seed. No one knows what to do with such a wonderful seed as this.",
			"title": "New Seed"
        }
        and poem like: {
            "id": 1,
			"seed_id": 1,
			"submitted_at": "Sat, 30 Jul 2022 15:27:00 GMT",
			"submitted_by_user_id": 1,
			"text": "This is the poem text."
        } """

    users = [user.serialize() for user in User.query.all()]

    return jsonify(users=users)


@app.get('/users/<int:user_id>')
def get_user(user_id):
    """Returns data on one user like:
    {
        "first_name": "Kate",
        "id": 1,
        "last_name": "Moser",
        "liked_poems": [poem, ...],
        "submitted_poems": [poem, ...]
        "submitted_seeds": [ seed, ...]
    } """

    user = User.query.get_or_404(user_id)

    return jsonify(user.serialize())


@app.get('/seeds')
def list_seeds():
    """Returns all seeds in system.

    returns JSON like:
    { seeds: [seed, ... ] }

    with seed like:
        {
            "author": "Kate",
			"id": 123,
			"poems_seeded": [ poem, ...],
			"submitted_at": "Sat, 30 Jul 2022 15:45:37 GMT",
			"submitted_by_user_id": 1,
			"text": "This seed is the best seed. No one knows what to do with such a wonderful seed as this.",
			"title": "New Seed"
        }
    and poem like: {
            "id": 1,
			"seed_id": 1,
			"submitted_at": "Sat, 30 Jul 2022 15:27:00 GMT",
			"submitted_by_user_id": 1,
			"text": "This is the poem text."
        } """

    seeds = [seed.serialize() for seed in Seed.query.all()]

    return jsonify(seeds=seeds)


@app.post('/seeds')
def create_seed():
    """Creates seed. returns JSON like:
        {seed: {
            "author": "Kate",
			"id": 123,
			"poems_seeded": [ poem, ...],
			"submitted_at": "Sat, 30 Jul 2022 15:45:37 GMT",
			"submitted_by_user_id": 1,
			"text": "This seed is the best seed. No one knows what to do with such a wonderful seed as this.",
			"title": "New Seed" }
        } """
    data = request.json
    print(data)

    seed = Seed(
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
    """Returns data on one seed like:

    {seed: {
            "author": "Kate",
			"id": 123,
			"poems_seeded": [ poem, ...],
			"submitted_at": "Sat, 30 Jul 2022 15:45:37 GMT",
			"submitted_by_user_id": 1,
			"text": "This seed is the best seed. No one knows what to do with such a wonderful seed as this.",
			"title": "New Seed" } """

    seed = Seed.query.get_or_404(seed_id)

    return jsonify(seed=seed.serialize())


@app.get('/seeds/<int:seed_id>/generate')
def generate_poem(seed_id):
    """Returns string of poem generated with seed_id like:

    "This is the new generated poem" """

    seed = Seed.query.get_or_404(seed_id)
    text_generator = MarkovMachine(seed.text)

    return text_generator.get_text()

# COMMENTING OUT FOR NOW WHILE IMPLEMENTING BLUEPRINT
# @app.get('/poems')
# def list_poems():
#     """Returns all Poems in system

#     returns JSON like:
#     {poems: [poem, ...] }
#     with poem like: {
#             "id": 1,
# 		    "seed_id": 1,
# 			"submitted_at": "Sat, 30 Jul 2022 15:27:00 GMT",
# 			"submitted_by_user_id": 1,
# 			"text": "This is the poem text."
#         } """

#     poems = [poem.serialize() for poem in Poem.query.all()]

#     return jsonify(poems=poems)


# @app.route('/poems', methods=["POST"])
# def create_poem():
#     """ Creates new Poem. Retruns JSON like:
#     {poem: {
#             "id": 1,
# 		    "seed_id": 1,
# 			"submitted_at": "Sat, 30 Jul 2022 15:27:00 GMT",
# 			"submitted_by_user_id": 1,
# 			"text": "This is the poem text."
#         } } """
#     data = request.json

#     poem = Poem(
#         seed_id= data['seed_id'],
#         text=data['text'],
#         submitted_by_user_id=1
#     )
#     db.session.add(poem)
#     db.session.commit()

#     return jsonify(poem=poem.serialize())


@app.get('/poems/<int:poem_id>')
def get_poem(poem_id):
    """returns JSON data on one poem like:
    {poem: {
            "id": 1,
		    "seed_id": 1,
			"submitted_at": "Sat, 30 Jul 2022 15:27:00 GMT",
			"submitted_by_user_id": 1,
			"text": "This is the poem text."
        } } """

    poem = Poem.query.get_or_404(poem_id)

    return jsonify(poem=poem.serialize())



###### HOROSCOPE ROUTES ##################################

@app.get('/horoscopes/daily/<sign>')
def get_daily_horoscope(sign):
    """ Returns JSON like:
    {horoscope: {
        "sign" : "pisces",
        "text" : "This is a generated horoscope"
    }}
    """

    seeds = HoroscopeSeed.get_todays_seeds(sign)

    seed_texts = [seed["text"] for seed in seeds]

    # add delimiter character, make machine
    input = " @ ".join(seed_texts)
    mm = MarkovMachine(input)

    generated_horoscope = mm.get_text()


    return jsonify(sign=sign, text=generated_horoscope)