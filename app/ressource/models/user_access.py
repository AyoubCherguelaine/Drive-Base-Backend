import json
from app import db
from datetime import datetime



class user_access(db.Model):
    __tablename__ = "rel_user_access"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey("users.id"), nullable=False)
    resource_id = db.Column(db.ForeignKey("resources.id"), nullable=False)
    access_id = db.Column(db.ForeignKey("access.id"), nullable=False)
    
    def __repr__(self):
        return "<user_access %r>" % self.id
    
    def __str__(self):
        return "user_access(%r, %r)" % (self.id, self.name)
    
    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }