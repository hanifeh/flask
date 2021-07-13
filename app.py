from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/', methods=['POST', 'get'])
def hello_world():
    # return 'Hello World!'
    return render_template('hello.html', name='sadegh')


@app.route('/hello/<name>/')
def hello(name):
    return f'Hello {escape(name)}'


@app.route('/num/<int:pk>/')
def hello_number(pk):
    return f'Hello {escape(pk)}'


if __name__ == '__main__':
    app.run()
