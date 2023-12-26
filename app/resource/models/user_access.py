import json
from app import db
from datetime import datetime



class user_access(db.Model):
    __tablename__ = "rel_user_access"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey("users.id"), nullable=False)
    resource_id = db.Column(db.ForeignKey("resources.id"), nullable=False)
    access_id = db.Column(db.ForeignKey("access.id"), nullable=False)
    
    resource = db.relationship("resource", lazy='joined', foreign_keys=[resource_id])
    user = db.relationship("User", lazy='joined', foreign_keys=[user_id])
    access = db.relationship("Access",lazy='joined', foreign_keys=[access_id])
    
    def __repr__(self):
        return "<user_access %r>" % self.id
    
    def __str__(self):
        return "user_access(%r, %r)" % (self.id, self.name)
    
    def json_populate(self):
        return {
            "id": self.id,
            "user": self.user.json(),
            "resource": self.resource.json(),
            "access": self.access.json()
        }
    
    def json(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "resource_id": self.resource_id,
            "access_id": self.access_id
        }