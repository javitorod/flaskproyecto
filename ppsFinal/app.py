from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random string"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column('id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(50))


    def __init__(self,name,password):
        self.name = name
        self.password = password
  
 

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hello/<name>')   
def hello(name):
    return 'welcome %s' % name

@app.route('/fluxer', methods=['GET'])
def fluxer_index():
    return('fluxer_index')

@app.route('/fluxer', methods=['POST'])
def fluxer_create():
    return('fluxer_create')

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)