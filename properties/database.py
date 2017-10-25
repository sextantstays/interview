import sqlite3

from flask import current_app as app
from flask import g

from bootstrap_fixtures import INITIAL_OWNERS
from bootstrap_fixtures import INITIAL_PROPERTIES

DATABASE = './database.db'


def init_db():
    """Initiates the database."""
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

    for owner in INITIAL_OWNERS:
        create_owner(owner)

    for property in INITIAL_PROPERTIES:
        create_property(property)


def get_db():
    """Gets a database object."""
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db


@app.teardown_appcontext
def close_connection(exception):
    """Close the database connection as the app terminates."""
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def query_db(query, args=(), one=False):
    """Wraps a database query."""
    with app.app_context():
        cur = get_db().execute(query, args)
        rv = cur.fetchall()
        cur.close()
        return (rv[0] if rv else None) if one else rv


def insert(table, fields=(), values=()):
    """Wraps an insertion into the db with fields and values."""
    with app.app_context():
        db = get_db()
        query = 'INSERT INTO %s (%s) VALUES (%s)' % (
            table,
            ', '.join(fields),
            ', '.join(['?'] * len(values))
        )
        db.execute(query, values)
        db.commit()
        db.close()


# ############# Property helper methods.


def create_property(property_info):
    """Insert a new property given a dictionary of property information."""
    return insert('property', property_info.keys(), property_info.values())


def get_all_properties():
    """Gets all stored properties."""
    properties = []
    for property in query_db('SELECT * FROM property;'):
        properties.append({
            'id': property['id'],
            'ownerId': property['ownerId'],
            'displayPictureUrl': property['displayPictureUrl'],
            'address': property['address'],
            'type': property['type'],
            'bedrooms': property['bedrooms'],
            'bathrooms': property['bathrooms'],
            'state': property['state'],
            'city': property['city'],
            'totalRevenue': property['totalRevenue'],
            'occupancyRate': property['occupancyRate'],
            'description': property['description'],
        })
    return properties


def get_property(id):
    """Gets an individual property by id."""
    property = query_db('SELECT * FROM property WHERE id = ?', [id], one=True)
    if not property:
        return {}

    return {
        'id': property['id'],
        'ownerId': property['ownerId'],
        'displayPictureUrl': property['displayPictureUrl'],
        'address': property['address'],
        'type': property['type'],
        'bedrooms': property['bedrooms'],
        'bathrooms': property['bathrooms'],
        'state': property['state'],
        'city': property['city'],
        'totalRevenue': property['totalRevenue'],
        'occupancyRate': property['occupancyRate'],
        'description': property['description'],
    }

# ############# Owner helper methods.


def create_owner(owner_info):
    """Insert a new owner given a dictionary of owner information."""
    return insert('owner', owner_info.keys(), owner_info.values())


def get_all_owners():
    """Gets all stored owners."""
    owners = []
    for owner in query_db('SELECT * FROM owner'):
        owners.append({
            'id': owner['id'],
            'firstName': owner['firstName'],
            'lastName': owner['lastName'],

        })
    return owners


def get_owner(id):
    """Gets an owner by id."""
    owner = query_db('SELECT * FROM owner WHERE id = ?', [id], one=True)
    if not owner:
        return {}

    return {
        'id': owner['id'],
        'firstName': owner['firstName'],
        'lastName': owner['lastName'],
    }
