"""Models for Blogly."""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """connect to database"""

    db.app = app
    db.init_app(app)


class User(db.Model):
    """User."""

    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.Text,
                           nullable=False)
    last_name = db.Column(db.Text,
                          nullable=False)
    image_url = db.Column(db.Text,
                          nullable=False)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Post(db.Model):
    """Post"""

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', backref=db.backref('posts'), lazy=True)


    # def __init__(self,title,content, user_id):
    #     self.title = title
    #     self.content = content
    #     self.user_id = user_id

def connect_db(app):

    db.app = app
    db.init_app(app)
