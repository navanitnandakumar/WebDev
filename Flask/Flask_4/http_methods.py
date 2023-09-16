from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return(render_template('index.html'))

#For 'GET' method, we render 'login.html'
#For 'POST' method, name is obtained from the form in 'login.html' and is assigned to the variable 'usr' and is redirected to 'user'

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == "POST":
        name = request.form['nm']
        return(redirect(url_for('user', usr = name)))
    else:
        return(render_template('login.html'))

@app.route('/<usr>')
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ == '__main__':
    app.run(debug = True)