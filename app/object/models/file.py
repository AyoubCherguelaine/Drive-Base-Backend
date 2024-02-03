import uuid
from app import db
from datetime import datetime
from flask import url_for

import os

from app.users.models.users import User
from app.resource.models.resources import resource
from app.resource.models.access import Access
from app.resource.models.user_access import user_access
from app.object_storage_system.models.buckets import bucket

class file(db.Model):
    __tablename__ = "files"
    id = db.Column(db.Integer, primary_key=True)
    object_id = db.Column(db.ForeignKey("objects.id"), nullable=False)
    file_name = db.Column(db.String(300))
    size_of_file = db.Column(db.Float)
    
    
    object = db.relationship("object", lazy='joined', foreign_keys=[object_id])
    
    #attr
    data_keys = {'object_id', 'file_name','size_of_file'}
    
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
    
    @staticmethod
    def upload_file(uploaded_file,user:User):
        try:
            datetime_upload = datetime.now()
            file_name, file_extension = os.path.splitext(uploaded_file.filename)
            unique_identifier = str(uuid.uuid4())  # Use a unique identifier for file naming
            
            name = f'{unique_identifier}___{user.id}__{datetime_upload}.{file_extension}'
            description = f"""
            user : {user.id}/{user.username}
            file : {uploaded_file.filename}
            date_upload : {datetime_upload}
            """
            # create a resrouce
            new_resource = resource(name,description)
            # access 'all' 'read'
            access = Access.get_access_by_name('All')
            # create a user access to resource with 'all'
            new_user_access = user_access(user.id,new_resource.id,access.id)
            
            # get the bucket 
            my_bucket = bucket.get_bucket_by_name(f'{user.username}_bucket')
            if not my_bucket:
                static_path = f'{url_for("static")}/bucket/{user.username}_bucket'
                my_bucket = bucket(f'{user.username}_bucket',static_path)
                db.session.add(my_bucket)
        
            # create an object 
            new_object = object(new_resource.id,file_name,file_extension,my_bucket.id)
        
            # Save the file to a desired location
            path = my_bucket.save_file_in_bucket(uploaded_file, new_object)

        
            new_object.path_in_local = path
            # create file in db
            new_file = file(new_object.id, uploaded_file.filename)
        
            # commit in db after success
            
            db.session.add(new_resource)
            db.session.add(new_user_access)
            db.session.add(new_object)
            db.session.add(new_file)
            db.session.commit()  
            
            return True
        except Exception as e :
            db.session.rollback()
            return f'Error uploading file: {str(e)}'