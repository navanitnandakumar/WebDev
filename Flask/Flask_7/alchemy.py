from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

app = Flask(__name__)
app.secret_key = 'nav123'
#database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#setting up a database
db = SQLAlchemy(app)

#database objects are represented using classes
class users(db.Model):
    #unique identifier for each entry
    _id = Column("id", Integer, primary_key=True)
    name = Column("name", String(100))
    email = Column("email", String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email

@app.route('/')
def home():
    return(render_template('index.html'))

#displays all database objects
@app.route('/view')
def view():
    if 'user' in session:
        return(render_template('view.html', values = users.query.all()))
    else:
        flash("You are not logged in !")
        return(redirect(url_for('login')))

#deletes user from database
@app.route('/delete')
def delete():
    if 'user' in session:
        user = session['user']
        email = session['email']
        found = users.query.filter_by(email = email).delete()
        db.session.commit()
        flash(f'{user}\'s info deleted successfully', 'info')
        return(redirect(url_for('logout')))
    else:
        flash("You are not logged in !")
        return(redirect(url_for('login')))

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        session['user'] = user

        #saving user name in database
        found = users.query.filter_by(name = user).first()
        if found:
            session['email'] = found.email
        else:
            usr = users(user, "")
            db.session.add(usr)
            db.session.commit()

        flash(f'{user} logged in successfully', 'info')
        return(redirect(url_for('user')))
    else:
        if 'user' in session:
            flash('Already logged in !', 'info')
            return(redirect(url_for('user')))
        else:
            flash('Please log in :-', 'info')
            return(render_template('login.html'))

@app.route('/user', methods = ['POST', 'GET'])
def user():
    email = None
    if 'user' in session:
        user = session['user']
        if request.method == 'POST':
            email = request.form['email']
            session['email'] = email

            #saving user email in database
            found = users.query.filter_by(name = user).first()
            found.email = email
            db.session.commit()

            flash('E-Mail saved successfully')
        else:
            if 'email' in session:
                email = session['email']
        return(render_template('user.html', email = email))
    else:
        flash("You are not logged in !")
        return(redirect(url_for('login')))

@app.route('/logout')
def logout():
    if 'user' in session:
        user = session['user']
        flash(f'{user} logged out successfully', 'info')
        session.pop('user', None)
        session.pop('email', None)
        return(redirect(url_for('login')))
    else:
        flash("You are not logged in !")
        return(redirect(url_for('login')))

if __name__ == '__main__':
    #creating database
    with app.app_context():
        db.create_all()
    app.run(debug = True)