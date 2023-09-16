from flask import Flask, render_template

app = Flask(__name__)

#'base.html' is the base template and 'child.html' inherits from it.
@app.route('/')
def home():
    return(render_template('child.html', content = 'Inheritance'))

if __name__ == '__main__':
    app.run(debug = True)