from flask import Flask, render_template
app = Flask(__name__)
app.debug=True

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

@app.route("/khaokho.html")
def khaokho():
    return render_template("web/khaokho.html") 

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
if __name__ == "__main__":
    app.run()
