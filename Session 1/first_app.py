from flask import Flask

app = Flask(__name__)

# creating first endpoint : homepage
@app.route("/")
@app.route("/home") #you can add multiple decorators simultaneously

def home(): # homepage
    return "<h1> Welcome to the home page! </h1>"

# second endpoint : about page
@app.route("/about") 
def about():
    return "<h1> Welcome to the about page! </h1>"

# third endpoint : welcome page - path parameter
@app.route("/welcome/<name>") # by default string is passed as a parameter
def welcome(name):
    return f"<h1>hi {name}, welcome to the welcome page</h1>"

@app.route('/add/<int:num>')  # passing an integer as a parameter
def add(num):
    return f"<h1> input ={num}, output = {num+10} </h1>"

@app.route("/add2/<int:num1>/<int:num2>")
def add2(num1, num2):
    return f"<h1>{num1} + {num2} = {num1+num2} </h1>"


if __name__ == "__main__": # ensures that when app.py module is imported in some other module, it does not automatically runs the app
    app.run(debug=True)