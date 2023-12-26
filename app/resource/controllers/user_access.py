from app import db
from ..models.user_access import user_access as User_access_model
from flask import request, jsonify, abort
from app.base.endpoint import endpoint
class endpoint(endpoint):
    body_data_keys = {"user_id","resource_id","access_id"}

    
    @staticmethod
    def is_qudery_data_valide(data)->bool:
        pass

    @staticmethod
    def create(data):
        if endpoint.is_body_data_valide(data,User_access_model.data_keys, create = True):
            user_access = User_access_model(
                user_id=data['user_id'],
                resource_id=data['resource_id'],
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
        List_user_access = User_access_model.query.order_by(User_access_model.id).all()
        user_access_list = [user_access.json() for user_access in List_user_access]
        return jsonify(user_access_list)   

    @staticmethod
    def get(id: str):
        user_access = User_access_model.query.first_or_404(id)
        return jsonify(user_access.json())
    
    @staticmethod
    def update(id: str,data):
        user_access = User_access_model.query.first_or_404(id)
        if endpoint.is_body_data_valide(data,User_access_model.data_keys):
            for key in list(data.keys()):
                setattr(user_access, key, data[key])
            try:
                db.session.commit()
                return jsonify(user_access.json())
            except Exception as e :
                abort(500,e)
        else:
            abort(400,{"Invalid user_access data"})
            
            
    @staticmethod       
    def delete(id):
        user_access = User_access_model.query.first_or_404(id)
        try:
            db.session.delete(user_access)
            db.session.commit()
            return {"result":"Deleted"}
        except Exception as e : 
            abort(500,e)
            
    @staticmethod
    def get_list_details(query=None):
        List_user_access = User_access_model.query.order_by(User_access_model.id).all()
        user_access_list = [user_access.json_populate() for user_access in List_user_access]
        return jsonify(user_access_list)  
    
    @staticmethod
    def get_details(id: str):
        user_access = User_access_model.query.first_or_404(id)
        return jsonify(user_access.json_populate())
