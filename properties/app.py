#!/usr/bin/env python
import datetime

from flask import Flask
from flask import jsonify
# from flask import request
from flask_cors import CORS


app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app, supports_credentials=True)
app.config['SECRET_KEY'] = 'top-secret!'
app.app_context().push()

# Load after we setup our app to avoid a circular import.
import database  # noqa

database.init_db()


def _add_dynamic_display_price(prop):
    """Create a price that fluctuates around an anchor, unique to each property."""
    base_rate = prop['totalRevenue'] * prop['occupancyRate'] * 1.00  # We anchor against totalRev
    time_mult = datetime.datetime.now().second / 5  # Ranges 0 - 11
    dynamic_price = round(base_rate + (time_mult * 25.00), 2)
    prop['dynamicDisplayPrice'] = dynamic_price
    return prop


@app.route('/properties/', methods=['GET'])
def get_all_properties():
    properties = database.get_all_properties()
    properties = [_add_dynamic_display_price(prop) for prop in properties]
    return jsonify(
        properties=properties,
        count=len(properties),
    )


@app.route('/properties/<property_id>/', methods=['GET'])
def get_property(property_id):
    prop = database.get_property(property_id)
    prop = _add_dynamic_display_price(prop)
    return jsonify(
        properties=prop
    )


# Uncomment to allow creating properties
# @app.route('/properties', methods=['POST'])
# @app.route('/properties/', methods=['POST'])
# def create_property():
#     database.create_property(request.json)
#     return jsonify(property=database.get_property(request.json['id']))


@app.route('/owners/', methods=['GET'])
def get_all_owners():
    owners = database.get_all_owners()
    return jsonify(
        owners=owners,
        count=len(owners),
    )


@app.route('/owners/<owner_id>/', methods=['GET'])
def get_owner(owner_id):
    return jsonify(owner=database.get_owner(owner_id))


# Uncomment to allow creating owners
# @app.route('/owners/', methods=['POST'])
# def create_owner():
#     database.create_owner(request.json)
#     return jsonify(owner=database.get_owner(request.json['id']))


if __name__ == '__main__':
    app.run(debug=True)
