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


class Seed(db.Model):
    """Seed Class for Markov API"""

    __tablename__ = "seeds"

    id = db.Column(
        db.Integer,
        primary_key=True,
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


class Poem(db.Model):
    """Machine generated poem class for Markov API"""

    __tablename__ = "poems"

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    seed_id = db.Column(
        db.Integer,
        db.ForeignKey('seeds.id')
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


class Like(db.Model):
    """Like on poem from user"""

    __tablename__ = "likes"

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        primary_key=True
    )

    poem_id = db.Column(
        db.Integer,
        db.ForeignKey('poems.id'),
        primary_key=True
    )


def connect_db(app):
    """Connect this database to provided Flask app.
    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)