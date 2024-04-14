from flask import Flask, jsonify, request, abort
from bookDAO import bookDAO

app = Flask(__name__, static_url_path='', static_folder='.')

#app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

#curl "http://127.0.0.1:5000/books"
@app.route('/books')
def getAll():
    #print("in getall")
    results = bookDAO.getAll()
    return jsonify(results)

#curl "http://127.0.0.1:5000/books/2"
@app.route('/books/<int:id>')
def findById(id):
    foundBook = bookDAO.findByID(id)

    return jsonify(foundBook)

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"title\":\"hello\",\"author\":\"someone\",\"price\":123}" http://127.0.0.1:5000/books
@app.route('/books', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    book = {
        "title": request.json['title'],
        "author": request.json['author'],
        "price": request.json['price'],
    }
    addedbook = bookDAO.create(book)
    
    return jsonify(addedbook)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"title\":\"hello\",\"author\":\"someone\",\"price\":123}" http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    foundBook = bookDAO.findByID(id)
    if not foundBook:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'price' in reqJson and type(reqJson['price']) is not int:
        abort(400)

    if 'title' in reqJson:
        foundBook['title'] = reqJson['title']
    if 'author' in reqJson:
        foundBook['author'] = reqJson['author']
    if 'price' in reqJson:
        foundBook['price'] = reqJson['price']
    bookDAO.update(id,foundBook)
    return jsonify(foundBook)
        

    

@app.route('/books/<int:id>' , methods=['DELETE'])
def delete(id):
    bookDAO.delete(id)
    return jsonify({"done":True})




if __name__ == '__main__' :
    app.run(debug= True)

# because I'm going to be do this on a different machine, I should set up a virtual environment to do that
# python -m venv venv
# source ./venv/bin/activate
# pip freeze (there should be nothing in there)
# pip install flask
# now we can run the server 
# if u do ls, u should see thhis file there
# run this file, in output, u will get: http://127.0.0.1:5000 (open in browser)

# running: Hello Ibu
# Crtl C
# now we push this up to GH

# So next thing we need to do is pull that down into a Python anywhere.
# on pythonanywhere dashboard, > console > Python > bash (this creates a new vrtual environment)
# on bash, git clone (code https for deploypythonanywhere repo) https://github.com/nurbujang/deploytopythonanywhere.git
# ls, u will see deploypythonanywhere in bash
# cd deploypythonanywhere, ls, u will see this .py file there

# next is to get this running on web apps and set up configuration, click the snake on top left bash
# on pythonanywhere dashboard, >web apps > open web tab > add a new web app
# let web app's domain name as nurbujang.pythonanywhere.com
# > flask > python 3.10 (maybe)
# let path /home/nurbujang/mysite/flask_app.py
# This site will be disabled on Saturday 13 July 2024

# Code:

# What your site is running.
# Source code:
# /home/nurbujang/mysite >>> change to /home/nurbujang/deploytopythonanywhere

# Working directory:
# /home/nurbujang/ >>> change to /home/nurbujang/deploytopythonanywhere

# WSGI configuration file:
# /var/www/nurbujang_pythonanywhere_com_wsgi.py
# Python version:
# 3.10

# goto nurbujang.pythonanywhere.com 
# goto WSGI configuration file: /var/www/nurbujang_pythonanywhere_com_wsgi.py

# yOU WILL SEE:
# This file contains the WSGI configuration required to serve up your
# web application at http://<your-username>.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#
# The below has been auto-generated for your Flask project

# import sys

# # add your project directory to the sys.path
# project_home = '/home/nurbujang/mysite'
# if project_home not in sys.path:
#     sys.path = [project_home] + sys.path

# # import flask app but need to call it "application" for WSGI to work
# from flask_app import app as application  # noqa

# CHANGE TO, then save:

# import sys

# # add your project directory to the sys.path
# project_home = '/home/nurbujang/mysite'
# if project_home not in sys.path:
#     sys.path = [project_home] + sys.path

# # import flask app but need to call it "application" for WSGI to work
# from server import app as application  # noqa

#SAVE! > go back click snake > web apps > open web tab > RELOAD nurbujang.pythonanywhere.com > 
# click nurbujang.pythonanywhere.com > will say Hello Ibu

# now connect with db >  go back to pythonanywhere dashboard
# n> consoles > more > other:MySQL > goto the databases tab to set Initialize MySQL > enter password

#  this sets up a database on the MySQL side, the Python anywhere machine. 
#And then you need to link to this with your server with the DAO.



# what abt the one uve already done? replace server containing Hello ibu with original server in original deploytopythonanywhere in lab



# > open server.py in deploytopythonanywhere inside wsaa-coursework/lab
# assuming u have a db already: 127.0.0.1:5000/bookviewer.html
# u need bookDAO.py, bookviewer.html, dbconfig_template.py, dbconfig.py together with server.py 
# push all files in the folder on github

#now goto server in deploy








# if error: ModuleNotFoundError: No module named 'mysql' in venv, pip install mysql-connector, then pip freeze > requirements.txt
# pip install flask, then pip freeze > requirements.txt
# http://127.0.0.1:5000 should get hello world
# http://127.0.0.1:5000/bookviewer.html should work
# push to github -m "real server"

# go back to pythonanywhere > Databases (top right corner) 
# create database, enter wsaa, so u will have Name nurbujang$default and nurbujang$wsaa
# password 7pa..*

# now create a table on this: click nurbujang$wsaa
# mysql > use nurbujang$wsaa
# show tables; Empty set
# create table book ( id int AUTO_INCREMENT PRIMARY KEY,
#                    author varchar(250),
#                    title varchar(250),
#                    price int);

# show tables;
# exit;

# go back to snake > Console > Bash console 33326338 (this will take the code down), so git pull
# 14:21 ~ $ cd deploytopythonanywhere
# 14:22 ~/deploytopythonanywhere (main)$ ls
# LICENSE  README.md  __pycache__  server.py
# 14:22 ~/deploytopythonanywhere (main)$ git pull
# remote: Enumerating objects: 9, done.
# remote: Counting objects: 100% (9/9), done.
# remote: Compressing objects: 100% (7/7), done.
# remote: Total 7 (delta 0), reused 7 (delta 0), pack-reused 0
# Unpacking objects: 100% (7/7), 4.60 KiB | 55.00 KiB/s, done.
# From https://github.com/nurbujang/deploytopythonanywhere
#    f57ca76..9f64fe9  main       -> origin/main
# Updating f57ca76..9f64fe9
# Fast-forward
#  bookDAO.py           | 104 ++++++++++++++++++
#  bookviewer.html      | 242 +++++++++++++++++++++++++++++++++++++++++
#  dbconfig.py          |   6 +
#  dbconfig_template.py |   6 +
#  server.py            |  91 +++++++++++++++-
#  5 files changed, 448 insertions(+), 1 deletion(-)
#  create mode 100644 bookDAO.py
#  create mode 100644 bookviewer.html
#  create mode 100644 dbconfig.py
#  create mode 100644 dbconfig_template.py
# 14:22 ~/deploytopythonanywhere (main)$ 

# vi dbconfig.py > will still have wrong data > exit

# so go to local machine, copy dbconfig.py and name it as dbconfigpa.py

# go back to pa > Databases (get info here and put in dbconfigpa.py)
# mysql = {
#     'host':"nurbujang.mysql.pythonanywhere-services.com",
#     'user':"nurbujang",
#     'password':"wsaapassword",
#     'database':"nurbujang$wsaa"
# }
# push on github
# pull on pa dashboard snake > Console > Bash console 33326338 and git pull
# 14:40 ~/deploytopythonanywhere (main)$ rm dbconfig.py
# 14:42 ~/deploytopythonanywhere (main)$ mv dbconfigpa.py dbconfig.py
# 14:42 ~/deploytopythonanywhere (main)$ less dbconfig.py (to view whats in the file, q to get out)

# go back to pa dash > Web apps > open web tab > Reload > refresh 
# nurbujang.pythonanywhere.com should say Hello Ibu
# https://nurbujang.pythonanywhere.com/bookviewer.html








 













