#!/usr/bin/env python

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top-secret!'
app.app_context().push()

import database  # noqa

database.init_db()


@app.route('/properties', methods=['GET'])
@app.route('/properties/', methods=['GET'])
def get_all_properties():
    return jsonify(properties=database.get_all_properties())


@app.route('/properties/<property_id>', methods=['GET'])
def get_property(property_id):
    return jsonify(properties=database.get_property(property_id))


@app.route('/properties', methods=['POST'])
@app.route('/properties/', methods=['POST'])
def create_property():
    database.create_property(request.json)
    return jsonify(property=database.get_property(request.json['id']))


@app.route('/owners', methods=['GET'])
@app.route('/owners/', methods=['GET'])
def get_all_owners():
    return jsonify(owners=database.get_all_owners())


@app.route('/owners/<owner_id>', methods=['GET'])
def get_owner(owner_id):
    return jsonify(owner=database.get_owner(owner_id))


@app.route('/owners', methods=['POST'])
@app.route('/owners/', methods=['POST'])
def create_owner():
    database.create_owner(request.json)
    return jsonify(owner=database.get_owner(request.json['id']))


if __name__ == '__main__':
    app.run(debug=True)
