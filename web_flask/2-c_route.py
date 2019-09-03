#!/usr/bin/python3
'''start a Flask web app
'''
from flask import Flask as fsk

app = fsk(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    '''root path
    '''
    return ("Hello HBNB!")


@app.route('/hbnb')
def hbnb():
    '''hbnb path
    '''
    return ("HBNB")


@app.route('/c/<text>')
def c_path(text):
    '''c plus text
    '''
    text.replace('_', ' ')
    return ("C {}".format(text))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
