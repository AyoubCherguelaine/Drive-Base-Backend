from app import db
from datetime import datetime

class extension(db.Model):
    __tablename__ = "extension"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    
    data_keys = {'name'}
    
    def __repr__(self) -> str:
        return "<extension %r>" % self.id
    
    def json(self):
        return {
            'id':self.id,
            'name':self.name
            }