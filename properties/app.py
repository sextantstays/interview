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


def _add_display_prices(prop, offset=0):
    """Create a price that fluctuates around an anchor, unique to each property."""
    increment_amount = 25.00
    time_mult = datetime.datetime.now().second / 5  # Ranges 0 - 11
    offset_mult = (time_mult + offset) % 12  # So that each property increments in price at an offset from each other

    base_price = prop['totalRevenue'] * prop['occupancyRate'] * 1.00  # We anchor against totalRev
    dynamic_price = (base_price - increment_amount) + (offset_mult * increment_amount)

    prop['basePrice'] = round(base_price, 2)
    prop['dynamicDisplayPrice'] = round(dynamic_price, 2)
    return prop


@app.route('/properties/', methods=['GET'])
def get_all_properties():
    properties = database.get_all_properties()
    properties = [_add_display_prices(prop, i) for i, prop in enumerate(properties)]
    return jsonify(
        properties=properties,
        count=len(properties),
    )


@app.route('/properties/<property_id>/', methods=['GET'])
def get_property(property_id):
    prop = database.get_property(property_id)
    prop = _add_display_prices(prop)
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
