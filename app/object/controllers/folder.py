from app import db
from ..models.folder import folder as Folder_
from flask import jsonify, abort
from app.base.endpoint import endpoint

class endpoint(endpoint):
    
    @staticmethod
    def create(data):
        if endpoint.is_body_data_valide(data,
                                        Folder_.data_keys,
                                        create=True):
            folder = Folder_(
                resource_id = data['resource_id'],
                parent_id = data['parent_id']
            )
            try:
                db.session.add(folder)
                db.session.commit()
                return jsonify(folder.json())
            except Exception as e:
                abort(500,e)
        else:
            abort(400 , {"message": "Invalid folder data" })

    
    @staticmethod
    def get_list(query):
        list_folders = Folder_.query.order_by(Folder_.id).all()
        folders = [folder.json() for folder in list_folders] 
        return jsonify(folders)
    
    @staticmethod
    def get(id):
        folder = Folder_.query.first_or_404(id)
        return jsonify(folder.json())
    
    @staticmethod
    def update(id,data):
        folder = Folder_.query.first_or_404(id)
        if endpoint.is_body_data_valide(data, Folder_.data_keys):
            for key in list(data.keys()):
                setattr(folder,key,data[key])
            try:
                db.session.commit()
                return jsonify(folder.json())
            except Exception as e :
                abort(500,e)
        else:
            abort(400,{"Invalid folder data"})
    
    @staticmethod
    def delete(id):
        folder = Folder_.query.first_or_404(id)
        try:
            db.session.delete(folder)
            db.session.commit()
            return {"result":"Deleted"}
        except Exception as e :
            abort(500,e)
    
    @staticmethod
    def get_list_details(query=None):
        list_folders = Folder_.query.order_by(Folder_.id).all()
        folders = [folder.json_populate() for folder in list_folders] 
        return jsonify(folders)
    
    @staticmethod
    def get_details(id):
        folder = Folder_.query.first_or_404(id)
        return jsonify(folder.json_populate())
    