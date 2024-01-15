from app import db
from datetime import datetime

class bucket(db.Model):
    __tablename__ = "buckets"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    
    def __repr__(self)->str:
        return "<bucket %r" % self.id
    
    def json(self):
        return {
            "id": self.id,
            "name": self.name
        }