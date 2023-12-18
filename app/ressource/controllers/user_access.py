from app import db
from ..models.user_access import user_access
from flask import request, jsonify, abort

class endpoint:
    
    @staticmethod
    def check_user_access_data(data,create=False)->bool:
        required_keys = {"user_id","ressource_id","access_id"}
        if create and set(data.keys()) == required_keys:
            return True
        elif not create and set(data.keys()) & required_keys:
            return True
        else:
            return False

    @staticmethod
    def create_user_access(data):
        if endpoint.check_user_access_data(data, create = True):
            user_access = user_access(
                user_id=data['user_id'],
                ressource_id=data['ressource_id'],
                access_id=data['access_id']
            )
            try:
                db.session.add(user_access)
                db.session.commit()
                return jsonify(user_access)
            except Exception as e:
                abort(500,e.message)
        else:
            abort(400 , {"message": "Invalid user_access data" })
        
    
    @staticmethod
    def get_list_user_access():
        List_user_access = user_access.query.order_by(user_access.id).all()
        user_access_list = [user_access.json() for user_access in List_user_access]
        return jsonify(user_access_list)   

    @staticmethod
    def get_user_access(id: str):
        user_access = user_access.query.first_or_404(id)
        return jsonify(user_access.json())
    
    @staticmethod
    def update_user_access(id: str,data):
        user_access = user_access.query.first_or_404(id)
        if endpoint.check_user_access_data(data):
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
    def delete_user_access(id):
        user_access = user_access.query.first_or_404(id)
        try:
            db.session.delete(user_access)
            db.session.commit()
            return True
        except Exception as e : 
            abort(500,e.message)