from webinfo import app
from flask import  render_template, flash, redirect, session, request, url_for
from .models import User, db, Contact, ReviewByUser
import os

__author__ = 'ibininja'


APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
@app.route("/index.html")
def index():
    username = session.get('username', '')
    session['username'] = username
    return render_template("index.html", username=username)

@app.route("/about_us.html")
def about_us():
    return render_template("web/about_us.html")

@app.route("/upload.html", methods=("GET", "POST"))
def upload():
#     test=""
#     target = os.path.join(APP_ROOT, './static/img/ImgUpload/')
#     print(target)
    
#     if not os.path.isdir(target):
#         os.mkdir(target)
#     for file in request.files.getlist("file"):
#         test="HELLO"
#         print(file)
#         filename = file.filename
#         destination = "/".join([target, filename])
#         print(destination)
        
#         file.save(destination)
      


    return render_template("user_Review.html")

    
@app.route("/user_Review.html", methods=("GET", "POST"))
def user_review():
    
    username = session.get('username', '')
    # session['username'] = username
    error = ""
    test = ""
    if not username:
        return redirect(url_for('.login'))

    if request.method == "POST":
        
        message_review = request.form["msg"] #msg name ของ Form ทีส่งมา message_review เป็นไรก็ได้
        go_date = request.form["goday"]
        back_date = request.form["backday"]
        money = request.form["money"]
        NameTrip = request.form["NameTrip"]
        if message_review == "" or go_date == "" or back_date=="":
            error = 'Please enter your field.'
        else:
            if error == "":
                test="test"
                try:
                    review = ReviewByUser(message=message_review,go_date=go_date,back_date=back_date,money=money,NameTrip = NameTrip,ImageName="") #ด้านหน้าเป็นแอตทริบิวเทเบิ้ล ด้านหลังเป็นค่าที่ส่งมจาก Form
                
                    db.session.add(review)
                    db.session.commit() 
                    # session['message'] = message
                    # flash('Register successfully.', 'success')
                    
                    target = os.path.join(APP_ROOT, './static/img/ImgUpload/')
                    print(target)
                    
                    if not os.path.isdir(target):
                        os.mkdir(target)
                    for file in request.files.getlist("file"):
                        test="HELLO"
                        print(file)
                        filename = file.filename
                        destination = "/".join([target, filename])
                        print(destination)
                        
                        file.save(destination)
                        
                    return redirect(url_for('.login'))
                except:
                    db.session.rollback()
                    error = "Something Wrong!"
    return render_template("user_Review.html",error=error,test=test,username=username)

@app.route("/contact.html", methods=("GET", "POST"))
def contact():
    error = ""
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        if name == "" or email == "" or message == "":
            error = "Please fill empty field."
        else:
            try:
                contact = Contact(name=name, email=email, message=message)
                db.session.add(contact)
                db.session.commit()
                flash("We got your message!!.", "success")
            except:
                db.session.rollback()
                error = "somthing wrong!!"
                flash('Something Wrong!', 'error')

    return render_template("/contact.html", error=error)

@app.route("/event.html")
def event():
    return render_template("web/event.html")
    
@app.route("/blog3.html")
def blog3():
    return render_template("/blog3.html")

@app.route("/blog6.html")
def blog6():
    return render_template("/blog6.html")

@app.route("/review1.html")
def review1():
    return render_template("/review1.html")

@app.route("/review2.html")
def review2():
    return render_template("/review2.html")


@app.route("/food.html")
def food():
    return render_template("web/food.html") 

@app.route("/blog2.html")
def blog2():
    return render_template("/blog2.html")

@app.route("/blog4.html")
def blog4():
    return render_template("/blog4.html")

@app.route("/blog5.html")
def blog5():
    return render_template("/blog5.html")

@app.route("/like.html")
def like():
    return render_template("/like.html")

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

@app.route("/blog1.html")
def blog1():
    return render_template("blog1.html")


app.secret_key = os.urandom(12)
@app.route("/login.html", methods=["GET","POST"])
def login():
    error = None
    username = session.get('username', '')
    password = session.get('password', '')
    if request.method == 'POST':
        if request.form['username'] == '' and request.form['password'] == '':
            error = 'Please enter your username and password.'
        elif request.form['username'] == '':
            error = 'Please enter your username'
        elif request.form['password'] == '':
            error = 'Please enter your password'
        else:
            users = User.query.all()
            for user in users:
                if request.form['password'] == user.password and request.form['username'] == user.username:
                    flash('Login successfully.', 'success')
                    if username:
                        session['username'] = username
                    else:
                        session['username'] = request.form['username']
                    return redirect(url_for('.index'))
                else:
                    error = 'Invalid username or password. Please try again.'
    return render_template('login.html', error=error, username=username, password=password)

@app.route("/register.html", methods=["GET","POST"])
def register():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == '' or password == '':
            error = 'Please enter your username or password'
        else:
            if error == None:
                try:
                    new_user = User(username=username,password=password)
                    db.session.add(new_user)
                    db.session.commit()
                    session['username'] = username #การได้ session มา !! แล้วไปดู login
                    session['password'] = password
                    flash('Register successfully.', 'success')
                    return redirect(url_for('.login'))
                except:
                    db.session.rollback()
                    error = "Username or Password already exists."
                    flash('Something Wrong!', 'error')
    return render_template("register.html", error=error)

@app.route('/logout')
def logout():
    session['username'] = ''
    flash('You were logged out')
    return redirect(url_for('index'))
    