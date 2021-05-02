#!/usr/bin/python3
''' flask code for '''

from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    ''' fancy hbnb site '''
    return render_template('10-hbnb_filters.html', state_list=storage.all(State),
                           amenities=storage.all(Amenity))


@app.teardown_appcontext
def remove_session(exception):
    ''' removes current SQLAlchemy Session '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
