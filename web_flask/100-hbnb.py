#!/usr/bin/python3
'''start a Flask web app
'''
from flask import Flask as fsk
from flask import render_template, abort
from models import storage

app = fsk(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
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
    try:
        state_dict = storage.all("State")
        cities_dict = storage.all("City")

        for k, v in state_dict.items():
            key = k.split('.')[1]
            if key == id:
                obj = state_dict[k]

        return(render_template('9-states.html',
                               cities=cities_dict, states=obj))
    except BaseException:
        return(render_template('9-states.html',
                               cities=cities_dict, states=None))


@app.route('/hbnb_filters')
def hbnb_filters():
    '''filters scroll
    '''

    state_dict = storage.all("State")
    cities_dict = storage.all("City")
    amenity_dict = storage.all("Amenity")

    return(render_template('10-hbnb_filters.html',
                           cities=cities_dict,
                           states=state_dict,
                           amenities=amenity_dict))


@app.route('/hbnb')
def hbnb():
    '''hbnb
    '''

    state_dict = storage.all("State")
    cities_dict = storage.all("City")
    amenity_dict = storage.all("Amenity")
    place_dict = storage.all("Place")

    return(render_template('100-hbnb.html',
                           cities=cities_dict,
                           states=state_dict,
                           amenities=amenity_dict,
                           places=place_dict))


@app.teardown_appcontext
def close_(exception=None):
    """close session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
