from app import db
from ..models.user_access import user_access
from flask import request, jsonify, abort
from app.base.endpoint import endpoint
class endpoint(endpoint):
    body_data_keys = {"user_id","ressource_id","access_id"}

    
    @staticmethod
    def is_qudery_data_valide(data)->bool:
        pass

    @staticmethod
    def create(data):
        if endpoint.is_body_data_valide(data,endpoint.body_data_keys, create = True):
            user_access = user_access(
                user_id=data['user_id'],
                ressource_id=data['ressource_id'],
                access_id=data['access_id']
            )
            try:
                db.session.add(user_access)
                db.session.commit()
                return jsonify(user_access.json())
            except Exception as e:
                abort(500,e)
        else:
            abort(400 , {"message": "Invalid user_access data" })
        
    
    @staticmethod
    def get_list(query=None):
        List_user_access = user_access.query.order_by(user_access.id).all()
        user_access_list = [user_access.json() for user_access in List_user_access]
        return jsonify(user_access_list)   

    @staticmethod
    def get(id: str):
        user_access = user_access.query.first_or_404(id)
        return jsonify(user_access.json())
    
    @staticmethod
    def update(id: str,data):
        user_access = user_access.query.first_or_404(id)
        if endpoint.is_body_data_valide(data,endpoint.body_data_keys):
            for key in list(data.keys()):
                setattr(user_access, key, data[key])
            try:
                db.session.commit()
                return jsonify(user_access.json())
            except Exception as e :
                abort(500,e.message)
        else:
            abort(400,{"Invalid user_access data"})
            
            
    @staticmethod       
    def delete(id):
        user_access = user_access.query.first_or_404(id)
        try:
            db.session.delete(user_access)
            db.session.commit()
            return {"result":"Deleted"}
        except Exception as e : 
            abort(500,e.message)