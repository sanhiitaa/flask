from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to the homepage stranger!</h1>"

@app.route("/pass/<sname>/<int:marks>")
def passs(sname, marks):
    return f"<h1>Congratulations {sname.title()}, you've passed with {marks} marks!</h1>"

@app.route("/fail/<sname>/<int:marks>")
def fail(sname, marks):
    return f"<h1>Sorry {sname.title()}, you've failed with {marks} marks!</h1>"


@app.route("/score/<name>/<int:num>")
def score(name, num):
    if num < 30 :
        # redirect to page fail
        return redirect(url_for("fail", sname=name, marks=num))
    else: 
        # redirect to page pass
        return redirect(url_for("passs", sname=name, marks=num)) 

if __name__=="__main__":
    app.run(debug=True) 