#importing flask
from flask import Flask

#creating an instance of a flask web app
app = Flask(__name__)

#defining the route to the page
@app.route("/")
#defining the page
def home():
    return "<h1>Hello world</h1>"

#similarly, we can define additional pages
@app.route("/<username>")
def greeting(username):
    return f"Hello {username} !"

#running the app
if __name__ == "__main__":
    app.run()