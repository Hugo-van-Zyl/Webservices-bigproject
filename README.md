# Web Services and Applications Big Project
By Hugo van Zyl

## About
This is my project for the Web Services and Applications module. Its basically a book manager where you can add books, edit them, delete them etc. It uses flask for the server and 
sqlite for the database. I went with sqlite instead of mysql cos its easier to set up, you dont need wamp running or anything like that and it works grand on pythonanywhere too.

### 1. Clone the repo
```
git clone https://github.com/Hugo-van-Zyl/Webservices-bigproject
```
Note open your terminal and cd into the filepath where you saved the above directory

### 2. Set up virtual environment
```
python -m venv venv
.\venv\Scripts\activate   (Windows)
source venv/bin/activate  (Mac/Linux)
pip install -r requirements.txt
```

### 3. Start the server
```
python rest_server.py
```
Should start on http://127.0.0.1:5000

### 4. Open it
Go to http://127.0.0.1:5000 in your browser and you should see the page.

## What it does
- You can add a new book (title, author, price)
- View all the books in a table
- Edit a book by clicking Edit
- Delete a book by clicking Delete

All of this is done through AJAX calls so the page doesnt reload every time.

## Files
- `rest_server.py` - the flask server, has all the API routes
- `bookdao.py` - does all the database stuff (the DAO from the labs)
- `staticpages/index.html` - the front end, uses bootstrap and ajax
- `requirements.txt` - install packages

## References
1. Lab 05.01 - Create a REST Server (Andrew Beatty)
2. Lab 06.02 - Python and Databases (Andrew Beatty)
3. Lab 03.01 - Requests (Andrew Beatty)
4. Flask docs - https://flask.palletsprojects.com/
5. Python sqlite3 docs - https://docs.python.org/3/library/sqlite3.html
6. Claude AI. 1) Please rewrite my Readme more professionally and concisely. 2) Please see the attached project description document and provide a full project structure outline and project ideas. 3) My html file is giving errors, please identify why and propose fixes
7. Bootstrap - https://getbootstrap.com/docs/5.3/
8. W3Schools AJAX - https://www.w3schools.com/js/js_ajax_intro.asp
9. W3Schools JS tutorial - https://www.w3schools.com/js/DEFAULT.asp