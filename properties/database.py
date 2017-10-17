import sqlite3

from flask import current_app as app
from flask import g

DATABASE = './database.db'

INITIAL_PROPERTIES = [
    {
        'displayPictureUrl': 'https://imgur.com/0700J1K',
        'address': '1 Castle Ave',
        'type': 'home',
        'bedrooms': 20,
        'bathrooms': 10,
        'state': 'Casterly Rock',
        'city': 'Citadel One',
        'totalRevenue': 10000.10,
        'occupancyRate': 0.6,
        'id': '410e409f-ac02-4afb-bbbe-8b7ff708647f',
        'ownerId': 'b7f065af-a43a-45ee-acff-bfa6757abf74',
    },
    {
        'displayPictureUrl': 'https://imgur.com/MXjhCKZ',
        'address': 'Round Home Alley',
        'type': 'home',
        'bedrooms': 1,
        'bathrooms': 1,
        'state': 'New York',
        'city': 'Farhook',
        'totalRevenue': 101.12,
        'occupancyRate': 0.50,
        'id': 'a02968b4-6608-4c15-a980-09cdb1c9c914',
        'ownerId': 'b7f065af-a43a-45ee-acff-bfa6757abf74',
    },
    {
        'displayPictureUrl': 'https://imgur.com/ViTP31Z',
        'address': 'Red Keep St.',
        'type': 'home',
        'bedrooms': 4,
        'bathrooms': 3,
        'state': 'California',
        'city': 'Red Hook',
        'totalRevenue': 7241.44,
        'occupancyRate': 0.85,
        'id': '8f82a5da-5013-42bf-b91e-0261302b6158',
        'ownerId': 'b7f065af-a43a-45ee-acff-bfa6757abf74',
    },
    {
        'displayPictureUrl': 'https://imgur.com/BLz3iqE',
        'address': 'Blue Lagoon Ave',
        'type': 'home',
        'bedrooms': 4,
        'bathrooms': 2,
        'state': 'Lagoon',
        'city': 'Ocean Blue',
        'totalRevenue': 3146.81,
        'occupancyRate': 0.68,
        'id': 'ebbbac58-e8d6-4a9b-95cb-d761619c0a6e',
        'ownerId': 'e34e507a-9663-4c17-b0dd-a2ea164bd33f',
    },
    {
        'displayPictureUrl': 'https://imgur.com/PU1b0sA',
        'address': 'P. Sherman 42 Wallaby Way',
        'type': 'apartment',
        'bedrooms': 2,
        'bathrooms': 1.5,
        'state': 'Florida',
        'city': 'Sidney',
        'totalRevenue': 3002.01,
        'occupancyRate': 0.77,
        'id': 'ffae9d3a-7925-4ea3-af25-4bac5c2fd19b',
        'ownerId': 'e34e507a-9663-4c17-b0dd-a2ea164bd33f',
    },
    {
        'displayPictureUrl': 'https://imgur.com/t9kiQDv',
        'address': '101 St Nicholas Dr',
        'type': 'home',
        'bedrooms': 1,
        'bathrooms': 1,
        'state': 'Alaska',
        'city': 'North Pole',
        'totalRevenue': 200.00,
        'occupancyRate': 0.99,
        'id': 'c92ff782-0e09-4aa2-a353-88d9422f46e7',
        'ownerId': 'b586b52a-c86a-40aa-9dec-0d2accb7e8cb',
    },
    {
        'displayPictureUrl': 'https://imgur.com/rb4cx4D',
        'address': '533-1 Otsu',
        'type': 'apartment',
        'bedrooms': 2,
        'bathrooms': 1,
        'state': 'Nagakute',
        'city': 'Ibaragabasama',
        'totalRevenue': 750.00,
        'occupancyRate': 0.90,
        'id': 'a07e8017-0b2f-4924-8df5-39f89766173d',
        'ownerId': 'b586b52a-c86a-40aa-9dec-0d2accb7e8cb',
    },
    {
        'displayPictureUrl': 'https://imgur.com/8ICyD0Z',
        'address': '2 Shoes Lane',
        'type': 'home',
        'bedrooms': 1,
        'bathrooms': 1,
        'state': 'Shoesicle',
        'city': 'Socksville',
        'totalRevenue': 1750.50,
        'occupancyRate': 0.74,
        'id': '901ee465-5772-4291-936a-c426959e3525',
        'ownerId': 'b586b52a-c86a-40aa-9dec-0d2accb7e8cb',
    },
    {
        'displayPictureUrl': 'https://imgur.com/SdhiKjC',
        'address': '124 Conch Street',
        'type': 'home',
        'bedrooms': 1,
        'bathrooms': 1,
        'state': 'Pacific Ocean',
        'city': 'Bikini Bottom',
        'totalRevenue': 550.50,
        'occupancyRate': 0.90,
        'id': 'b7c198f7-ca13-41d1-9c40-75dfd71fffde',
        'ownerId': 'b586b52a-c86a-40aa-9dec-0d2accb7e8cb',
    },
    {
        'displayPictureUrl': 'https://imgur.com/dESVdup',
        'address': '742 Evergreen Terrace',
        'type': 'home',
        'bedrooms': 2,
        'bathrooms': 1,
        'state': 'Colorado',
        'city': 'Springfield',
        'totalRevenue': 420.00,
        'occupancyRate': 0.83,
        'id': 'e637b315-bc36-43d0-aa15-83f341a8f962',
        'ownerId': '9d1863f4-de8d-47ff-a534-391b25f5f021',
    },
]

INITIAL_OWNERS = [
    {
        'id': 'b7f065af-a43a-45ee-acff-bfa6757abf74',
        'firstName': 'Bruce',
        'lastName': 'Wayne',
    },
    {
        'id': 'c882770e-46bd-48d5-b7ad-ed66392c7839',
        'firstName': 'Slim',
        'lastName': 'Shady',
    },
    {
        'id': 'e34e507a-9663-4c17-b0dd-a2ea164bd33f',
        'firstName': 'Sarah',
        'lastName': 'Sahara',
    },
    {
        'id': 'b586b52a-c86a-40aa-9dec-0d2accb7e8cb',
        'firstName': 'Eliza',
        'lastName': 'Burton',
    },
    {
        'id': '9d1863f4-de8d-47ff-a534-391b25f5f021',
        'firstName': 'Bob',
        'lastName': 'Ross',
    },
]


def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

    for owner in INITIAL_OWNERS:
        create_owner(owner)

    for property in INITIAL_PROPERTIES:
        create_property(property)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def query_db(query, args=(), one=False):
    with app.app_context():
        cur = get_db().execute(query, args)
        rv = cur.fetchall()
        cur.close()
        return (rv[0] if rv else None) if one else rv


def insert(table, fields=(), values=()):
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
    return insert('property', property_info.keys(), property_info.values())


def get_all_properties():
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
        })
    return properties


def get_property(id):
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
    }

# ############# Owner helper methods.


def create_owner(owner_info):
    return insert('owner', owner_info.keys(), owner_info.values())


def get_all_owners():
    owners = []
    for owner in query_db('SELECT * FROM owner'):
        owners.append({
            'id': owner['id'],
            'firstName': owner['firstName'],
            'lastName': owner['lastName'],

        })
    return owners


def get_owner(id):
    owner = query_db('SELECT * FROM owner WHERE id = ?', [id], one=True)
    if not owner:
        return {}

    return {
        'id': owner['id'],
        'firstName': owner['firstName'],
        'lastName': owner['lastName'],
    }
