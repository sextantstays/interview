# Properties Portal
This application contains the API for our properties portal.

We use a basic Flask setup with two resources.
`/properties` and `/properties/<property_id>` lets us get property information.
`/owners` and `/owners/<owner_id>` lets us get owner information.


## Quickstart
1. Clone the [interview repository](https://github.com/staydomio/interview)
2. Go to the `properties` challenge: `cd properties`.
3. Install [pip](https://pip.pypa.io/en/stable/installing/) and [virtualenv](https://virtualenv.pypa.io/en/stable/installation/) if needed
4. Create a virtualenv, source the environment, install requirements
5. Start the Flask application: `env/bin/python setup.py install && env/bin/python app.py`
6. Go to `http://localhost:5000/properties` to test getting a list of properties

```bash
# Installing app dependencies
git clone https://github.com/staydomio/interview.git
cd interview
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
```bash
# Starting the Flask app
env/bin/python setup.py install && env/bin/python app.py
```

## What's included
* A simple [Flask](http://flask.pocoo.org/) app with the following endpoints:
  * GET `/properties`: Gets a list of all properties
  * GET `/properties/<property_id>`: Gets a single property by id
  * POST `/properties`: Create a new property
  * GET `/owners`: Gets a list of all property owners
  * GET `/owners/<owners_id>`: Gets a single owner by id
  * POST `/owners`: Create a new owner
  

## Requests, examples
```bash
# Create a new owner
curl -X POST -H "Content-Type: application/json" -d '{"firstName": "Rick", "lastName": "Sanchez", "id": "34f47dba-1013-4f79-b6f9-3ba4ec44c48e"}' http://127.0.0.1:5000/owners/```
```bash
# Create a new property
curl -X POST -H "Content-Type: application/json" -d '{"ownerId": "34f47dba-1013-4f79-b6f9-3ba4ec44c48e", "displayPictureUrl": "https://imgur.com/ViTP31Z", "address": "Red Keep St.", "type": "home", "bedrooms": 3, "bathrooms": 2.5, "state": "New York", "city": "New York City", "totalRevenue": 5100.00, "occupancyRate": 0.95, "id": "f73729f8-0fc6-4fc2-bfe6-f564f10ff907"}' http://127.0.0.1:5000/properties/
```
  

## Other requirements
* Depends on: Python 2.7.10
* All endpoints inputs and responses are in JSON


## Submitting Results
To submit your code clone this repo, commit your changes, and push to a new public remote repository.
Document any changes you've made either in the `README.md` or in a new documents file.
Document your code with comments where appropriate.
