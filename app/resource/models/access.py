import json
from app import db
from datetime import datetime

class Access(db.Model):
    __tablename__ = "access"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(500))
    
    #attr
    data_keys = {"name","description"}
    def __repr__(self):
        return "<access %r>" % self.id
    
    def __str__(self):
        return "access(%r, %r)" % (self.id, self.name)
    
    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }