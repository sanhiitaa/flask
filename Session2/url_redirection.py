from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to the homepage stranger!</h1>"

@app.route("/pass")
def passs():
    return "<h1>Congratulations, you've passed!</h1>"

@app.route("/fail")
def fail():
    return "<h1>Sorry, you've failed!</h1>"


@app.route("/score/<name>/<int:num>")
def score(name, num):
    if num < 30 :
        # redirect to page fail
        return redirect(url_for("fail"))
    else: 
        # redirect to page pass
        return redirect(url_for("passs")) 

if __name__=="__main__":
    app.run(debug=True) 