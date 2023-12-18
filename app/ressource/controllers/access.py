from app import db
from ..models.access import Access
from flask import request, jsonify, abort

class endpoint:
    
    @staticmethod
    def check_access_data(data,create=False)->bool:
        required_keys = {"name","description"}
        if create and set(data.keys()) == required_keys:
            return True
        elif not create and set(data.keys()) & required_keys:
            return True
        else:
            return False

    @staticmethod
    def create_access(data):
        if endpoint.check_access_data(data, create = True):
            access = Access(
                name=data['name'],
                description=data['description']
            )
            try:
                db.session.add(access)
                db.session.commit()
                return jsonify(access)
            except Exception as e:
                abort(500,e.message)
        else:
            abort(400 , {"message": "Invalid access data" })
        
    
    @staticmethod
    def get_list_access():
        List_access = Access.query.order_by(Access.id).all()
        access_list = [access.json() for access in List_access]
        return jsonify(access_list)   

    @staticmethod
    def get_access(id: str):
        access = Access.query.first_or_404(id)
        return jsonify(access.json())
    
    @staticmethod
    def update_access(id: str,data):
        access = Access.query.first_or_404(id)
        if endpoint.check_access_data(data):
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
    def delete_access(id):
        access = Access.query.first_or_404(id)
        try:
            db.session.delete(access)
            db.session.commit()
            return True
        except Exception as e : 
            abort(500,e.message)