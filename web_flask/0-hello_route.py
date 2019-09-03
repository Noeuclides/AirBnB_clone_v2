#!/usr/bin/python3
'''start a Flask web app
'''
from flask import Flask as fsk

app = fsk(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    return ("Hello HBNB!")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
