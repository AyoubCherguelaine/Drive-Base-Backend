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
from .object import object as Object_system
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
            datetime_upload = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file_name, file_extension = os.path.splitext(uploaded_file.filename)
            unique_identifier = str(uuid.uuid4())  # Use a unique identifier for file naming
            
            name = f'{unique_identifier}___{user.id}__{datetime_upload}.{file_extension}'
            description = f"""
            user : {user.id}/{user.username}
            file : {uploaded_file.filename}
            date_upload : {datetime_upload}
            """
            # create a resrouce
            new_resource = resource(
                **{"name":name,
                   "description":description}
                )
            db.session.add(new_resource)
            db.session.commit()  
            # access 'all' 'read'
            access = Access.get_access_by_name('All')
            
            # create a user access to resource with 'all'

            new_user_access = user_access(
                **{"user_id":user.id,
                "resource_id":new_resource.id,
                "access_id":access.id}
                )
            db.session.add(new_user_access)
            db.session.commit()  
                        
            # get the bucket 
            my_bucket = bucket.get_bucket_by_name(f'{user.username}_bucket')
            if not my_bucket:
                static_path = f'/home/ayoub/Desktop/Repos/WebBase/static/buckets/{user.username}_bucket'
                my_bucket = bucket(
                    **{"name":f'{user.username}_bucket',
                    "local_path":static_path}
                    )
                my_bucket.create_bucket()
                db.session.add(my_bucket)
                db.session.commit()  
        
            # create an object 
            new_object = Object_system(
                **{"resource_id":new_resource.id,
                "file_name":name,
                "file_extension":file_extension,
                "bucket_id":my_bucket.id}
                )
            
        
            # Save the file to a desired location
            path = my_bucket.save_file_in_bucket(uploaded_file, new_object)

        
            new_object.path_in_local = path
            db.session.add(new_object)
            db.session.commit()  
            # create file in db
            new_file = file(
                **{"object_id":new_object.id,
                "file_name":file_name}
                )
        
            db.session.add(new_file)
            db.session.commit()  
            
            return new_file
        except Exception as e :
            db.session.rollback()
            raise f'Error uploading file: {str(e)}'