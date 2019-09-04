#!/usr/bin/python3
'''start a Flask web app
'''
from flask import Flask as fsk
from flask import render_template
from models import storage

app = fsk(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    '''list cities in state
    '''
    state_dict = storage.all("State")
    return(render_template('7-states_list.html', states=state_dict))


@app.teardown_appcontext
def close_():
    """close session
    """
    storage.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
