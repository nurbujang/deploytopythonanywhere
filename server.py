from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello Ibu"

if __name__ == "__main__":
    app.run(debug = True)

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



# what abt the one uve already done? > open server.py in deploytopythonanywhere inside wsaa-coursework/lab
# assuming u have a db already: 127.0.0.1:5000/bookviewer.html
# u need bookDAO.py, bookviewer.html, dbconfig_template.py, dbconfig.py together with server.py 
# push all files in the folder on github

#now goto server in deploy


















