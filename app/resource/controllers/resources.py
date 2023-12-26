from app import db
from ..models.resources import resource as Resource
from flask import request, jsonify, abort
from app.base.endpoint import endpoint

class endpoint(endpoint):
    body_data_keys= {"name","description"}

    @staticmethod
    def create(data):
        if endpoint.is_body_data_valide(data, endpoint.body_data_keys, create = True):
            resource = Resource(
                name=data['name'],
                description=data['description']
            )
            try:
                db.session.add(resource)
                db.session.commit()
                return jsonify(resource.json())
            except Exception as e:
                abort(500,e)
        else:
            abort(400 , {"message": "Invalid resource data" })
        
    
    @staticmethod
    def get_list():
        resources = Resource.query.order_by(Resource.id).all()
        resource_list = [resource.json() for resource in resources]
        return jsonify(resource_list)   

    @staticmethod
    def get(id: str):
        resource = Resource.query.first_or_404(id)
        return jsonify(resource.json())
    
    @staticmethod
    def update(id: str,data):
        resource = Resource.query.first_or_404(id)
        if endpoint.is_body_data_valide(data, endpoint.body_data_keys):
            for key in list(data.keys()):
                setattr(resource, key, data[key])
            try:
                db.session.commit()
                return jsonify(resource.json())
            except Exception as e :
                abort(500,e.message)
        else:
            abort(400,{"Invalid resource data"})
            
            
    @staticmethod       
    def delete(id):
        resource = Resource.query.first_or_404(id)
        try:
            db.session.delete(resource)
            db.session.commit()
            return {"result":"Deleted"}
        except Exception as e : 
            abort(500,e.message)