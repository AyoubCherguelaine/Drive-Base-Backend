from app import db
from datetime import datetime
import os
from werkzeug.utils import secure_filename
class bucket(db.Model):
    __tablename__ = "buckets"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    local_path = db.Column(db.String(800))
    
    #attr bucket
    data_keys = {"name","local_path"}
    
    def __repr__(self)->str:
        return "<bucket %r" % self.id
    
    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            'local_path':self.local_path
        }
        
    def create_bucket(self):
        os.makedirs(self.local_path, exist_ok=True)
        
    def save_file_in_bucket(self, file):
        filename = secure_filename(file.filename)
        path = os.path.join(self.local_path, filename)
        file.save(path)
        return path
    
    def list_files_in_bucket(self):
        pass