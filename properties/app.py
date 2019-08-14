#!/usr/bin/env python

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


@app.route('/properties/', methods=['GET'])
def get_all_properties():
    properties = database.get_all_properties()
    return jsonify(
        properties=properties,
        count=len(properties),
    )


@app.route('/properties/<property_id>/', methods=['GET'])
def get_property(property_id):
    return jsonify(
        properties=database.get_property(property_id)
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
