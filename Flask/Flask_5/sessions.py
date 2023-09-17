from flask import Flask, render_template, request, redirect, url_for, session
from datetime import timedelta

app = Flask(__name__)

#sessions are temporary and stored on the web server
#it enables easy and quick access of information between pages
#sessions require a secret key

app.secret_key = "navnan1290"

#defining the lifetime of a session
app.permanent_session_lifetime = timedelta(minutes = 2)

@app.route('/')
def home():
    return(render_template('index.html'))

@app.route('/login', methods = ['GET', 'POST'])
def form():
    if request.method == 'POST':
        #defining session as permanent is going to make it last as long as mentioned above
        session.permanent = True
        user = request.form['nm']
        session['user'] = user
        return(redirect(url_for('user')))
    else:
        if 'user' in session:
            return(redirect(url_for('user')))
        else:
            return(render_template('form.html'))

@app.route('/user')
def user():
    if 'user' in session:
        user = session['user']
        return f"<h1>{user}</h1>"
    else:
        return(redirect(url_for('form')))

#deleting sessions
@app.route('/logout')
def delete():
    session.pop('user', None)
    return(redirect(url_for('form')))

if __name__ == '__main__':
    app.run(debug = True)