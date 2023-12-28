from app import db
from datetime import datetime

class folder(db.Model):
    
    __tablename__ = "folders"
    id = db.Column(db.Integer, primary_key=True)
    resource_id = db.Column(db.ForeignKey("resources.id"), nullable=False)
    parent_id = db.Column(db.ForeignKey("folders.id"), nullable=False)
    
    # Define relationships with the related models
    resource = db.relationship("resource", lazy='joined', foreign_keys=[resource_id])
    parent_folder = db.relationship("folder", lazy='joined', foreign_keys=[parent_id])

    #attr
    data_keys = {"resource_id","parent_id"}
    
    def __repr__(self) -> str:
        return "<folder %r" % self.id
    
    def json_populated(self):
        return {
            "id": self.id,
            "resource_id": self.resource.json(),
            "parent_id": self.parent_folder.json_populated()
        }
      
    def json(self):
        return {
            "id": self.id,
            "resource_id": self.resource_id,
            "parent_id": self.parent_id
        }
        
