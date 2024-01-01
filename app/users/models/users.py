import json
from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    
    firstname = db.Column(db.String(200))
    lastname = db.Column(db.String(200))
    username = db.Column(db.String(200))
    email = db.Column(db.String(200))
    password = db.Column(db.String(200))
    active = db.Column(db.Boolean,default=0)
    
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    data_keys = {'firstname',
                 'lastname',
                 'username',
                 'email',
                 'password',
                 'active'}
    
    def __repr__(self):
        return "<user %r>" % self.id
    
    def __str__(self):
        return "user %r { username : %r , email : %r}" % self.id , self.username, self.email, self.email
    
    def json(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "username": self.username,
            "email": self.email
        }
    
    