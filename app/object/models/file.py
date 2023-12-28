from app import db
from datetime import datetime

class file(db.Model):
    __tablename__ = "files"
    id = db.Column(db.Integer, primary_key=True)
    object_id = db.Column(db.ForeignKey("objects.id"), nullable=False)

    object = db.relationship("object", lazy='joined', foreign_keys=[object_id])
    
    #attr
    data_keys = {'object_id'}
    
    def __repr__(self) -> str:
        return "<file %r" % self.id
    
    def json_populate(self):
        return {
            "id": self.id,
            "object": self.object.json_populate()
        }
    
    def json(self):
        return {
            "id": self.id,
            "object_id": self.object_id
        }
        