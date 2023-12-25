from app import db
from datetime import datetime

class file(db.Model):
    __tablename__ = "files"
    id = db.Column(db.Integer, primary_key=True)
    object_id = db.Column(db.ForeignKey("objects.id"), nullable=False)

    
    def __repr__(self) -> str:
        return "<file %r" % self.id
    
    def json(self):
        return {
            "id": self.id,
            "object_id": self.object_id
        }
        
