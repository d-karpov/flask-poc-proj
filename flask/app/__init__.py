from flask import Flask
# import os

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_SORT_KEYS'] = False
# app.config['X-API-KEY'] = os.getenv('X-API-KEY')
app.config['X-API-KEY'] = '123321'

from app import views
