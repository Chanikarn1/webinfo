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

class ReviewByUser(db.Model):
    go_date= db.Column(db.String(10), nullable=False, primary_key=False)
    back_date= db.Column(db.String(10), nullable=False, primary_key=False)
    message = db.Column(db.String(100000), nullable=False, primary_key=True)
    money = db.Column(db.String(10), nullable=False, primary_key=False)
    NameTrip = db.Column(db.String(255), nullable=False, primary_key=True)
    ImageName = db.Column(db.String(255), nullable=True, primary_key=False)
    def __init__(self, message,go_date,back_date,money,NameTrip,ImageName):
        # self.username = godate
        self.message = message  
        self.go_date = go_date #ด้านหน้า global ด้านหลัง local
        self.back_date = back_date
        self.money = money
        self.NameTrip = NameTrip
        self.ImageName = ImageName
        
