from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///C:\\Users\\ESOUSSH\\Downloads\\Personal\\Github\\Practices\\Languages\\Python\\Python\\Flask\\flask.db'
db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80),unique=True)
    email=db.Column(db.String(120),unique=True)

    def __init__(self,username,email):
        self.username=username
        self.email=email

    def __repr__(self):
        return '<User %r>'%self.username

@app.route('/')
def index():
    return '<h1>Hello Sourab</h1>'
if __name__=='__main__':
    app.run()