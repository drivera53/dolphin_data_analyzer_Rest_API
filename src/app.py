# Using flask to make an api 
# import necessary libraries and functions 
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from dateutil import parser
from members.models import DB_PATH, db, IgUsers, IgPosts
from utils.analyzer import process_Ig_Users_Posts
  
# creating a Flask app 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DB_PATH

db.init_app(app)
  
# on the terminal type: curl http://127.0.0.1:5000/ 
# returns hello world when we use GET. 
# returns the data that we send when we use POST. 
@app.route('/', methods = ['GET', 'POST']) 
def home(): 
    if(request.method == 'GET'):
        data = "Hello world"

        return jsonify({'data': data}) 
  
  
# A simple function to calculate the square of a number 
# the number to be squared is sent in the URL when we use GET 
# on the terminal type: curl http://127.0.0.1:5000/home/10 
# this returns 100 (square of 10) 
@app.route('/igdata/<int:apikey>', methods = ['GET']) 
def disp(apikey): 
    print(apikey) # To validate later
    db.create_all()
    all_ig_posts = IgPosts.query.all()
    all_ig_users = IgUsers.query.all()
    response = process_Ig_Users_Posts(all_ig_users, all_ig_posts)

    return jsonify({'data': response}) 
  
  
# driver function 
if __name__ == '__main__': 
    with app.app_context():
        app.run(debug = True)