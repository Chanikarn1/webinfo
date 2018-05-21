import os
from webinfo import app
from flask import Flask
from flask import render_template
from flask import request

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "users.db"))

app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
db.init_app(app)

class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return "<Username: {}>".format(self.username)

class Contact(db.Model):
    name = db.Column(db.String(80), nullable=False, primary_key=True)
    email = db.Column(db.String(80), nullable=False, primary_key=True)
    message = db.Column(db.String(80), nullable=False, primary_key=True)

    def __init__(self, name, email, message):
        self.name = name
        self.email = email
        self.message = message

class clientreview(db.Model):
    # godate= db.Column(db.String(80), nullable=False, primary_key=True)
    message = db.Column(db.String(100000), nullable=False, primary_key=True)
    def __init__(self, message):
        # self.username = godate
        self.message = message