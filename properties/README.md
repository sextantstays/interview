# Properties Portal
This application contains the API for our properties portal.

We use a basic Flask setup with two resources.
`/properties` and `/properties/<property_id>` lets us get property information.
`/owners` and `/owners/<owner_id>` lets us get owner information.


## Quickstart
1. Clone the [interview repository](https://github.com/staydomio/interview)
2. Go to the `properties` challenge: `cd properties`.
3. Install [pip](https://pip.pypa.io/en/stable/installing/) and [virtualenv](https://virtualenv.pypa.io/en/stable/installation/) if needed
4. Create a virtualenv and install requirements
5. Start the Flask application: `env/bin/python app.py`
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
env/bin/python app.py
```

## What's included
* A simple [Flask](http://flask.pocoo.org/) app with the following endpoints:
  * `/properties`: Gets a list of all properties
  * `/properties/<property_id>`: Gets a single property by id
  * `/owners`: Gets a list of all property owners
  * `/owners/<owners_id>`: Gets a single owner by id


## Other requirements
* Depends on: Python 2.7.10


## Submitting Results
To submit your code clone this repo, commit your changes, and push to a new public remote repository.
Document any changes you've made either in the `README.md` or in a new documents file.
Document your code with comments where appropriate.
