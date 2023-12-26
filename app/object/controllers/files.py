from app import db
from ..models.file import file as File_
from flask import jsonify, abort
from app.base.endpoint import endpoint

class endpoint(endpoint):
    
    @staticmethod
    def create(data):
        if endpoint.is_body_data_valide(data,
                                        File_.data_keys,
                                        create=True):
            file = File_(
                object_id = data['object_id']
            )
            try:
                db.session.add(file)
                db.session.commit()
                return jsonify(file.json())
            except Exception as e:
                abort(500,e)
        else:
            abort(400 , {"message": "Invalid File data" })

    
    @staticmethod
    def get_list(query):
        list_files = File_.query.order_by(File_.id).all()
        files = [file.json() for file in list_files] 
        return jsonify(files)
    
    @staticmethod
    def get(id):
        file = File_.query.first_or_404(id)
        return jsonify(file.json())
    
    @staticmethod
    def update(id,data):
        file = File_.query.first_or_404(id)
        if endpoint.is_body_data_valide(data, File_.data_keys):
            for key in list(data.keys()):
                setattr(file,key,data[key])
            try:
                db.session.commit()
                return jsonify(file.json())
            except Exception as e :
                abort(500,e)
        else:
            abort(400,{"Invalid file data"})
    
    @staticmethod
    def delete(id):
        file = File_.query.first_or_404(id)
        try:
            db.session.delete(file)
            db.session.commit()
            return {"result":"Deleted"}
        except Exception as e :
            abort(500,e)
    
    @staticmethod
    def get_list_details(query=None):
        list_files = File_.query.order_by(File_.id).all()
        files = [file.json_populate() for file in list_files] 
        return jsonify(files)
    
    @staticmethod
    def get_details(id):
        file = File_.query.first_or_404(id)
        return jsonify(file.json_populate())
    