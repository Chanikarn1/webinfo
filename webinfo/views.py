from webinfo import app
from flask import render_template, flash, redirect, session, request
from .models import User
import os

@app.route("/")
@app.route("/index.html")

def index():
    return render_template("web/index.html")

@app.route("/about_us.html")
def about_us():
    return render_template("web/about_us.html")

@app.route("/contact.html")
def contact():
    return render_template("web/contact.html")

@app.route("/event.html")
def event():
    return render_template("web/event.html")

@app.route("/food.html")
def food():
    return render_template("web/food.html")  
@app.route("/join.html")
def join():
    return render_template("web/join.html")


@app.route("/layout.html")
def layout():
    return render_template("layout.html") 

@app.route("/kohchang.html")
def kohchang():
    return render_template("web/kohchang.html") 

@app.route("/kohtao.html")
def kohtao():
    return render_template("web/kohtao.html") 

@app.route("/monjong.html")
def monjong():
    return render_template("web/monjong.html") 

@app.route("/phukradueng.html")
def phukradueng():
    return render_template("web/phukradueng.html")  

@app.route("/sutongpe.html")
def sutongpe():
    return render_template("web/sutongpe.html")  
@app.route("/test.html")
def test():
    return render_template("web/test.html")  

@app.route("/test2.html")
def test2():
    return render_template("web/test2.html")  

@app.route("/travel.html")
def travel():
    return render_template("web/travel.html")  


@app.route("/nav.html")
def test4():
    return render_template("nav.html")

app.secret_key = os.urandom(12)
@app.route("/login.html", methods=["GET", "POST"])
def login():
    users = User.query.all()
    for user in users:
        if request.form['password'] == user.password and request.form['username'] == user.username:
            session['logged_in'] = True
        else:
            flash('wrong password!')
    return index()

@app.route('/dashboard.html')
def dashboard():
    return render_template('dashboard.html')
