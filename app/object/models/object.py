from app import db
from datetime import datetime

class object(db.Model):
    __tablename__ = "objects"
    id = db.Column(db.Integer, primary_key=True)
    resource_id = db.Column(db.ForeignKey("resources.id"), nullable=False)
    file_name = db.Column(db.String(1000))
    file_extension =  db.Column(db.String(20))
    bucket_id = db.Column(db.ForeignKey("buckets.id"), nullable=False)
    path_in_local =  db.Column(db.String(1000))
    
    #relation
    resource = db.relationship("resource", lazy='joined', foreign_keys=[resource_id])
    bucket = db.relationship("bucket", lazy='joined', foreign_keys=[bucket_id])
    #attr object
    data_keys = {"resource_id","file_name","file_extension",'bucket_id'}
    
    def __repr__(self) -> str:
        return "<object %r" % self.id
    
    def json_populate(self):
        return {
            "id": self.id,
            "resource": self.resource.json(),
            "file_name": self.file_name,
            "file_extension": self.file_extension,
            'bucket':self.bucket.json()
        }
    
    def json(self):
        return {
            "id": self.id,
            "resource_id": self.resource_id,
            "file_name": self.file_name,
            "file_extension": self.file_extension,
            'bucket_id':self.bucket_id
        }
        