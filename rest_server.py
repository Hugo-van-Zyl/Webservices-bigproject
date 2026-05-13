# rest_server.py
# this is the flask server, it has all the url routes for the API
# based off lab 05.01 but i added the database stuff using bookdao
# https://flask.palletsprojects.com/en/2.3.x/quickstart/
 
from flask import Flask, request, jsonify, abort
 
import bookdao

# static_folder is where the html page lives
app = Flask(__name__, static_url_path='', static_folder='staticpages')
 
# when you go to the root url it just gives you the html page
@app.route('/')
def index():
    return app.send_static_file('index.html')