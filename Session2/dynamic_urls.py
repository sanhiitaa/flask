from flask import Flask

app= Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to the homepage stranger!</h1>"

@app.route("/<name>")
def welcome(name):
    return f"<h1>{name.title()}, welcome to our homepage!</h1>"

if __name__=="__main__":
    app.run(debug=True)