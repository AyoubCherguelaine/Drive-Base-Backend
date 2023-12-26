from app import db
from ..models.object import object as Object_
from flask import jsonify, abort
from app.base.endpoint import endpoint


class endpoint(endpoint):
    
    @staticmethod 
    def create(data):
        if endpoint.is_body_data_valide(data,Object_.data_keys,create=True):
            object = Object_(
                resource_id = data['resource_id'],
                path = data["path"]
            )
            try:
                db.session.add(object)
                db.session.commit()
                return jsonify(object.json())
            except Exception as e:
                abort(500,e)
        else:
            abort(400 , {"message": "Invalid object data" })

    @staticmethod
    def get_list(query):
        list_objects = Object_.query.order_by(Object_.id).all()
        objects = [object.json() for object in list_objects] 
        return jsonify(objects)
    
    @staticmethod
    def get(id):
        object = Object_.query.first_or_404(id)
        return jsonify(object.json())
    
    @staticmethod
    def update(id, data):
        object = Object_.query.first_or_404(id)
        if endpoint.is_body_data_valide(data, Object_.data_keys):
            for key in list(data.keys()):
                setattr(object,key,data[key])
            try:
                db.session.commit()
                return jsonify(object.json())
            except Exception as e :
                abort(500,e)
        else:
            abort(400,{"Invalid object data"})

    @staticmethod
    def delete(id):
        object = Object_.query.first_or_404(id)
        try:
            db.session.delete(object)
            db.session.commit()
            return {"result":"Deleted"}
        except Exception as e :
            abort(500,e)

        
    @staticmethod
    def get_list_details(query=None):
        list_objects = Object_.query.order_by(Object_.id).all()
        objects = [object.json_populate() for object in list_objects] 
        return jsonify(objects)
    
    @staticmethod
    def get_details(id):
        object = Object_.query.first_or_404(id)
        return jsonify(object.json_populate())