from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

'''
@app.route('/test')
def hello_world():
    return 'joke world'

@app.route('/test')
def whatever():
    a = "round"
    return render_template('index.html',shape = a)
'''

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'GET':
        return render_template('forms/text_analytics.html')
    elif request.method == 'POST':
        kwargs = {
            'first_document': request.form['first_document'],
            'second_document': request.form['second_document'],
            'author': request.form['author'],
            'secret_key': request.form['SECRET_KEY'],
            'submit_value': request.form['submit'],
        }
        return render_template(
            'forms/text_analytics_result.html', **kwargs)