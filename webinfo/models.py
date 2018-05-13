import os
from webinfo import app
from flask import Flask
from flask import render_template
from flask import request

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "user.db"))

app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
db.init_app(app)

class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

    def __repr__(self):
        return "<Username: {}>".format(self.username)
    