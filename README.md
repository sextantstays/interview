# Kitten Counter
This application contains important work in our mission to count all the kittens.

We use a basic Flask + Celery + Redis setup with one background task `count_kittens`.
An endpoint at `/kittens` lets us see the total number of kittens counted.


## Quickstart
1. Clone the [interview repository](https://github.com/staydomio/interview)
2. Create a virtualenv and install requirements
3. Open a new terminal and start a Redis server (use `run-redis.sh` to install and launch a private copy)
4. In a new terminal start a Celery worker: `env/bin/celery worker -A app.celery --loglevel=info`
5. In a new terminal start the Flask application: `env/bin/python app.py`
6. Go to `http://localhost:5000/kittens` and enjoy counting kittens!

```bash
# Installing app dependencies
git clone https://github.com/staydomio/interview.git
cd interview
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
```bash
# Installing and running redis
chmod +x run-redis.sh
./run-redis.sh
```
```bash
# Starting the Flask app
env/bin/python app.py
```
```bash
# Starting the Celery Worker
env/bin/celery worker -A app.celery -B --loglevel=info
```

## What's included
* A simple [Flask](http://flask.pocoo.org/) app with three endpoints:
  * `/`: Landing page
  * `/kittens`: Displays the number of kittens counted
* [Celery](http://docs.celeryproject.org/en/latest/getting-started/introduction.html) task queue with one task:
  * `count_kittens`: Increments a kitten counter every X seconds.
* [Redis](https://redis.io/) data store:
  * `kitten_counter`: Tracked key metric of number of kittens counted so far.



## Submitting Results
To submit your code clone this repo, commit your changes, and push to a new public remote repository.
Document any changes you've made either in the `README.md` or in a new documents file.
Document your code with comments where appropriate.
