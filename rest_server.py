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

 # curl -X POST -H "Content-Type:application/json" -d '{"title":"test","author":"me","price":10}' http://127.0.0.1:5000/books
@app.route('/books', methods=['POST'])
def create():
    # the book data comes in as json in the body of the request
    if not request.json:
        abort(400) # bad request, no json sent
    book = {
        "title": request.json["title"],
        "author": request.json["author"],
        "price": request.json["price"]
    }
    result = bookdao.create(book)
    return jsonify(result)
 
# curl -X PUT -H "Content-Type:application/json" -d '{"title":"new title","author":"me","price":20}' http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    if not request.json:
        abort(400)
    book = {
        "title": request.json["title"],
        "author": request.json["author"],
        "price": request.json["price"]
    }
    result = bookdao.update(id, book)
    return jsonify(result)
 
# curl -X DELETE http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    bookdao.delete(id)
    return jsonify({"done": True})
 
if __name__ == "__main__":
    bookdao.init_db() # set up the table before we start
    app.run(debug=True)