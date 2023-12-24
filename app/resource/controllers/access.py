from app import db
from ..models.access import Access
from flask import request, jsonify, abort
from app.base.endpoint import endpoint

class endpoint(endpoint):
    body_data_keys =  {"name","description"}
 
    @staticmethod
    def create(data):
        if endpoint.is_body_data_valide(data,endpoint.body_data_keys, create = True):
            access = Access(
                name=data['name'],
                description=data['description']
            )
            try:
                db.session.add(access)
                db.session.commit()
                return jsonify(access.json())
            except Exception as e:
                abort(500,e)
        else:
            abort(400 , {"message": "Invalid access data" })
        
    
    @staticmethod
    def get_list(query=None):
        List_access = Access.query.order_by(Access.id).all()
        access_list = [access.json() for access in List_access]
        return jsonify(access_list)   

    @staticmethod
    def get(id: str):
        access = Access.query.first_or_404(id)
        return jsonify(access.json())
    
    @staticmethod
    def update(id: str,data):
        access = Access.query.first_or_404(id)
        if endpoint.is_body_data_valide(data,endpoint.body_data_keys):
            for key in list(data.keys()):
                setattr(access, key, data[key])
            try:
                db.session.commit()
                return jsonify(access.json())
            except Exception as e :
                abort(500,e.message)
        else:
            abort(400,{"Invalid access data"})
            
            
    @staticmethod       
    def delete(id):
        access = Access.query.first_or_404(id)
        try:
            db.session.delete(access)
            db.session.commit()
            return {"result","Deleted"}
        except Exception as e : 
            abort(500,e.message)