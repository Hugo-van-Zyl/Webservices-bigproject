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

# curl http://127.0.0.1:5000/books
@app.route('/books', methods=['GET'])
def getall():
    # gets all books and sends them back as json
    results = bookdao.getAll()
    return jsonify(results)
 
# curl http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>', methods=['GET'])
def findbyid(id):
    book = bookdao.findByID(id)
    if book:
        return jsonify(book)
    else:
        abort(404) # book not found