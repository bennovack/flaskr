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
