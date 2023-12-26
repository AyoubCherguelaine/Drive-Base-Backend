import json
from app import db
from datetime import datetime

class resource(db.Model):
    __tablename__ = "resources"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50) )
    description = db.Column(db.String(200) )
    
    #attr
    data_keys = {"name","description"}
    
    def __repr__(self):
        return "<resource %r>" % self.id
    
    def __str__(self):
        return "resource(%r, %r)" % (self.id, self.name)
    
    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }