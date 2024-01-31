from app import db
from datetime import datetime

class folder(db.Model):
    
    __tablename__ = "folders"
    id = db.Column(db.Integer, primary_key=True)
    resource_id = db.Column(db.ForeignKey("resources.id"), nullable=False)
    parent_id = db.Column(db.ForeignKey("folders.id"), nullable=False)
    name=  db.Column(db.String(300))
    
    # Define relationships with the related models
    resource = db.relationship("resource", lazy='joined', foreign_keys=[resource_id])
    parent_folder = db.relationship("folder", lazy='joined', foreign_keys=[parent_id])

    #attr
    data_keys = {"resource_id","parent_id",'name'}
    
    def __repr__(self) -> str:
        return "<folder %r" % self.id
    
    def json_populated(self):
        return {
            "id": self.id,
            "resource": self.resource.json(),
            "parent": self.parent_folder.json_populated(),
            'name':self.name
        }
      
    def json(self):
        return {
            "id": self.id,
            "resource_id": self.resource_id,
            "parent_id": self.parent_id,
            "name": self.name
        }
        
