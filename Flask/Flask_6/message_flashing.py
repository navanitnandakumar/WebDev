from flask import Flask, render_template, redirect, url_for, request, session, flash

app = Flask(__name__)
app.secret_key = 'nav123'

@app.route('/')
def home():
    return(render_template('index.html'))

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        session['user'] = user
        flash(f'{user} logged in successfully', 'info')
        return(redirect(url_for('user')))
    else:
        if 'user' in session:
            flash('Already logged in !', 'info')
            return(redirect(url_for('user')))
        else:
            flash('You are not logged in !', 'info')
            return(render_template('login.html'))

@app.route('/user')
def user():
    if 'user' in session:
        user = session['user']
        return(render_template('user.html', user = user))
    else:
        return(redirect(url_for('login')))

@app.route('/logout')
def logout():
    #flashing a message when we log out
    if 'user' in session:
        user = session['user']
        flash(f'{user} logged out successfully', 'info')
    session.pop('user', None)
    #add message code in 'login.html'
    return(redirect(url_for('login')))

if __name__ == '__main__':
    app.run(debug = True)