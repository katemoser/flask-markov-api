"""Seed database for Markov"""

from app import db
from models import User, Seed, Like, Poem

db.drop_all()
db.create_all()

admin = User(
    id=1,
    username="kate",
    first_name="Kate",
    last_name="Moser"
)

db.session.add(admin)
db.session.commit()

seed = Seed(
    id=1,
    title="seed title",
    text="This is the seed text.",
    author="anonymous",
    submitted_by_user_id=1,
)

db.session.add(seed)
db.session.commit()

poem = Poem(
    id=1,
    seed_id=1,
    text="This is the poem text.",
    submitted_by_user_id=1
)

db.session.add(poem)
db.session.commit()

like = Like(
    user_id=1,
    poem_id=1,
)

db.session.add(like)
db.session.commit()
