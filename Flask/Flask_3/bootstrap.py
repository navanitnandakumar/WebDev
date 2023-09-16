from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return(render_template('bootstrap_base.html'))

@app.route('/child')
def child():
    return(render_template('bootstrap_child.html'))

if __name__ == '__main__':
    app.run(debug = True)