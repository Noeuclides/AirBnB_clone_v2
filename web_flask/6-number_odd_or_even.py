#!/usr/bin/python3
'''start a Flask web app
'''
from flask import Flask as fsk
from flask import redirect, url_for, abort, render_template

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


@app.route('/python')
@app.route('/python/<text>')
def python_path(text=None):
    '''python plus text
    '''
    if text is None:
        return(redirect(url_for('python_path', text='is cool')))
    else:
        text.replace('_', ' ')
        return ("Python {}".format(text))


@app.route('/number/<n>')
def number(n):
    '''number path
    '''
    try:
        return("{} is a number".format(int(n)))
    except BaseException:
        abort(404)


@app.route('/number_template/<n>')
def number_template(n):
    '''template path
    '''
    try:
        n = int(n)
        return(render_template('5-number.html', name=n))
    except BaseException:
        abort(404)


@app.route('/number_odd_or_even/<n>')
def number_odd_or_even(n):
    '''template path
    '''
    try:
        n = int(n)
        return(render_template('6-number_odd_or_even.html', number=n))
    except BaseException: 
        abort(404)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
