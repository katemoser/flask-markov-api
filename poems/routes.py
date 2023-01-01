from flask import Blueprint, jsonify, request

from models import db, Poem

poems = Blueprint('poems', __name__, url_prefix='/poems')

@poems.get('/')
def list_poems():
    """Returns all Poems in system
    
    returns JSON like: 
    {poems: [poem, ...] }
    with poem like: {
            "id": 1,
		    "seed_id": 1,
			"submitted_at": "Sat, 30 Jul 2022 15:27:00 GMT",
			"submitted_by_user_id": 1,
			"text": "This is the poem text."
        } """

    poems = [poem.serialize() for poem in Poem.query.all()]

    return jsonify(poems=poems)


@poems.route('/', methods=["POST"])
def create_poem():
    """ Creates new Poem. Retruns JSON like: 
    {poem: {
            "id": 1,
		    "seed_id": 1,
			"submitted_at": "Sat, 30 Jul 2022 15:27:00 GMT",
			"submitted_by_user_id": 1,
			"text": "This is the poem text."
        } } """
    data = request.json

    poem = Poem(
        seed_id= data['seed_id'],
        text=data['text'],
        submitted_by_user_id=1
    )
    db.session.add(poem)
    db.session.commit()

    return jsonify(poem=poem.serialize())

