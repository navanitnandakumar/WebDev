from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Redirects</h1>"

#if user goes to '/forbidden', it gets redirected to 'home'
@app.route("/forbidden")
def admin():
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run()