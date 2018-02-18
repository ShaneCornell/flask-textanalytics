from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/test')
def hello_world():
    return 'hello world'

@app.route('/')
def whatever():
    a = "round"
    return render_template('index.html',shape = a)