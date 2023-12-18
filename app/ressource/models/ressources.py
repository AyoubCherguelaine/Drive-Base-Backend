import json
from app import db
from datetime import datetime

class Ressource(db.Model):
    __tablename__ = "ressources"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50) )
    description = db.Column(db.String(200) )
    
    def __repr__(self):
        return "<ressource %r>" % self.id
    
    def __str__(self):
        return "ressource(%r, %r)" % (self.id, self.name)
    
    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }