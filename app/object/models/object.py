from app import db
from datetime import datetime

class object(db.Model):
    __tablename__ = "objects"
    id = db.Column(db.Integer, primary_key=True)
    resource_id = db.Column(db.ForeignKey("resources.id"), nullable=False)
    path = db.Column(db.String(1000))
    
    resource = db.relationship("resource", lazy='joined', foreign_keys=[resource_id])
    
    
    def __repr__(self) -> str:
        return "<object %r" % self.id
    
    def json_populate(self):
        return {
            "id": self.id,
            "resource": self.resource.json(),
            "path": self.path
        }
    
    def json(self):
        return {
            "id": self.id,
            "resource_id": self.resource_id,
            "path": self.path
        }
        
    def update_path(self, new_path):
        self.path = new_path
        db.session.commit()
        return self.json()