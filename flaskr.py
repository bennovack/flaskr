#http://flask.pocoo.org/docs/0.10/tutorial/dbcon/#tutorial-dbcon
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing

#config
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'dev key'
USERNAME = 'admin'
PASSWORD = 'default'

#create the app!
app = Flask(__name__)
app.config.from_object(__name__)
#TODO, change to:
#app.config.from_envar('FLASKR_SETTINGS', silent=True)


#Database Setup

def connect_db():
        return sqlite3.connect(app.config['DATABASE'])

def init_db():
        with closing(connect_db()) as db:
            with app.open_resource('schema.sql', mode='r') as f:
                db.cursor().executescript(f.read())
            db.commit()



if __name__ == '__main__':
        app.run()
#TODO: Check out http://flask.pocoo.org/docs/0.10/quickstart/#public-server
#Make it publically available
