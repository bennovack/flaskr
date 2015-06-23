# http://flask.pocoo.org/docs/0.10/tutorial/setup/#tutorial-setup

import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

#config
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'dev key'
USERNAME = 'admin'
PASSWORD = 'default'

#create the app!
app = Flask(__name__)
app.config.from_object(__name__)
#later, change to:
#app.config.from_envar('FLASKR_SETTINGS', silent=True)


def connect_db():
        return sqlite3.connect(app.config['DATABASE'])

if __name__ == '__main__':
        app.run()
