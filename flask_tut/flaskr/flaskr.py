# all the imports
from contextlib import closing
import sqlite3

from flask import Flask
from flask import request
from flask import session
from flask import g
from flask import redirect
from flask import url_for
from flask import abort
from flask import render_template
from flask import flash


# configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True # controls debugger; do not use in production!!!
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'


# create our little application :)
app = Flask(__name__)
# config.from_object gets all the UPPERCASE variable names in its arg
# and uses them to populate config, which is a dict (well, a Config, 
# a subclass of dict)
# 
# could also use config.from_envar, which works similarly; loads 
# UPPERCASE variable names in the config file that the environment 
# variable passed in as an arg.
app.config.from_object(__name__)


def connect_db():
    # we get 'DATABASE' (the variable DATABASE, defined above) into 
    # app's config dict by using from_object! neat, huh?
    return sqlite3.connect(app.config['DATABASE'])


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


# before_request gets called after a request gets made
@app.before_request
def before_request():
    g.db = connect.db()


# teardown_request gets called after a response to a request has been 
# created;
# after_request :: body of try block (might fail/raise an exception)
# teardown_request :: finally block after the try block
@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


@app.route('/')
def show_entries():
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [ dict(title=row[0], text=row[1]) for row in cur.fetchall() ]
    return render_template('show_entries.html', entries=entries)


if __name__ == '__main__':
    # use host kwarg to change whether it's public or not.
    app.run()
