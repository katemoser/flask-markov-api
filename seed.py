"""Seed database for Markov"""

from app import db
from models import User, Seed, Like, Poem

db.drop_all()
db.create_all()

