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
    '''list states
    '''
    state_dict = storage.all("State")
    return(render_template('7-states_list.html', states=state_dict))


@app.route('/cities_by_states')
def cities_list():
    '''list cities in state
    '''
    state_dict = storage.all("State")
    cities_dict = storage.all("City")
    return(render_template('8-cities_by_states.html',
                           cities=cities_dict, states=state_dict))

@app.route('/states/<id>')
def states_id(id):
    '''list state by id
    '''
    state_dict = storage.all("State")
    cities_dict = storage.all("City")
    print(type(id))

    for k, v in state_dict.items():
        print("KEY: ", k.split('.')[1])
        print()
        print("VALUE", v)
    return(render_template('9-states.html',
                           cities=cities_dict, states=state_dict))



@app.teardown_appcontext
def close_(exception=None):
    """close session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
