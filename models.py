"""Models for flask-markov"""

import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """User class for Markov API"""

    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
    )

    username = db.Column(
        db.Text,
        nullable=False
    )

    first_name = db.Column(
        db.Text,
        nullable=False
    )

    last_name = db.Column(
        db.Text,
        nullable=False
    )

    liked_poems = db.relationship(
        "Poem",
        secondary="likes",
        backref="liked_by_users"
    )

    submitted_poems = db.relationship(
        "Poem",
    )

    submitted_seeds = db.relationship(
        "Seed",
    )

    def serialize(self):
        """serialize user info"""

        return {
            "id": self.id,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "submitted_seeds": [seed.serialize() for seed in self.submitted_seeds],
            "submitted_poems": [poem.serialize() for poem in self.submitted_poems],
            "liked_poems": [poem.serialize() for poem in self.liked_poems],
        }


class Seed(db.Model):
    """Seed Class for Markov API"""

    __tablename__ = "seeds"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,

    )

    title = db.Column(
        db.Text,
        nullable=False,
    )

    text = db.Column(
        db.Text,
        nullable=False,
    )

    author = db.Column(
        db.Text,
        nullable=False,
    )

    submitted_by_user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id')
    )

    submitted_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.datetime.now
    )

    poems_seeded = db.relationship(
        "Poem"
    )

    def serialize(self):
        """serialize user info"""

        return {
            "id": self.id,
            "title": self.title,
            "text": self.text,
            "author": self.author,
            "submitted_by_user_id": self.submitted_by_user_id,
            "submitted_at": self.submitted_at,
            # "poems_seeded": [poem.serialize() for poem in self.poems_seeded]
        }


class Poem(db.Model):
    """Machine generated poem class for Markov API"""

    __tablename__ = "poems"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,

    )

    seed_id = db.Column(
        db.Integer,
        db.ForeignKey('seeds.id')
    )

    text = db.Column(
        db.Text,
        nullable=False
    )

    submitted_by_user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id')
    )

    submitted_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.datetime.now
    )

    def serialize(self):
        """serialize user info"""

        return {
            "id": self.id,
            "seed_id": self.seed_id,
            "text": self.text,
            "submitted_by_user_id": self.submitted_by_user_id,
            "submitted_at": self.submitted_at,
        }

    ################ HOROSCOPE! #############


class HoroscopeSeed(db.Model):

    __tablename__ = "horoscope_seeds"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
    )

    type = db.Column(
        db.String,
        nullable=False
    )

    sign_name = db.Column(
        db.String,
        db.ForeignKey("signs.name"),
        nullable=False
    )

    text = db.Column(
        db.Text,
        nullable=False
    )

    source = db.Column(
        db.String,
        nullable=False
    )

    date = db.Column(
        db.Date,
        nullable=False,
        default=datetime.datetime.utcnow().date()
    )

    @classmethod
    def get_todays_seeds(cls, sign):
        """"Takes an astrological sign and returns all daily seeds from today"""

        today = datetime.datetime.utcnow().date()
        print("TODAY", today)
        todays_seeds = cls.query.filter(
            cls.sign_name == sign
        ).filter(cls.date == today).all()

        serialized = [s.serialize() for s in todays_seeds]

        return serialized

    def serialize(self):
        return {
            "id": self.id,
            "sign": self.sign_name,
            "text": self.text,
            "date": self.date,
            "type": self.type
        }


class Sign(db.Model):
    """An astrological sign"""

    __tablename__ = "signs"

    name = db.Column(
        db.String,
        primary_key=True
    )

    horoscopes = db.relationship(
        'HoroscopeSeed',
        backref='sign',
        cascade='all, delete'
    )


class Like(db.Model):
    """Like on poem from user"""

    __tablename__ = "likes"

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        primary_key=True,

    )

    poem_id = db.Column(
        db.Integer,
        db.ForeignKey('poems.id'),
        primary_key=True,
        autoincrement=True,

    )


def connect_db(app):
    """Connect this database to provided Flask app.
    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)
