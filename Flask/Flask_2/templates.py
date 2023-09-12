from flask import Flask, render_template

app = Flask(__name__)

#create a folder called 'templates' which will store the html files
#'templates' folder must be in the same directory as this python file

@app.route("/")
def home():
    return render_template("index.html") #provide the name of the html file to render here

@app.route("/<name>")
def greeting(name):
    return render_template("greet.html", username = name, n = 'hi')

@app.route("/even")
def even_nums():
    return render_template("even.html")

@app.route("/odd")
def odd_nums():
    return render_template("odd.html")

@app.route("/list")
def list_func():
    return render_template("list.html", l = ["Tom", "Dick", "Harry"])

if __name__ == "__main__":
    app.run()