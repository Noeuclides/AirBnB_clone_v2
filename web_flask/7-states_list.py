#!/usr/bin/python3
'''start a Flask web app
'''
from models import storage
from flask import Flask as fsk
from flask import redirect, url_for, abort, render_template

app = fsk(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    '''list cities in state
    '''
#    try:
    state_dict = storage.all("State")
    return(render_template('7-states_list.html', states=state_dict))
#    except BaseException:
#        abort(404)

@app.teardown_appcontext
def close:
    """close session
    """
    storage.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
