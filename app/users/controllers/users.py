from app import db
from app.base.endpoint import endpoint
from ..models.users import User
from flask import request, jsonify, abort

class endpoint(endpoint):
    body_data_keys =  {'firstname', 'lastname', 'username', 'email', 'password'}
        
    @staticmethod
    def create(data):
        if endpoint.is_body_data_valide(data,endpoint.body_data_keys, create=True):
            user = User(firstname=data['firstname'], 
                        lastname=data['lastname'],
                        username=data['username'],
                        email=data['email'],
                        password=data['password'])
            try:
                db.session.add(user)
                db.session.commit()
                return jsonify(user.json())
            except Exception as e:
                abort(500,e)
        else:
            abort(400, {"message": "Invalid user data" })
    
    @staticmethod
    def get_list(query=None):
        users = User.query.order_by(User.id).all()
        users_list = [user.json() for user in users]
        return jsonify(users_list)

    @staticmethod
    def get(id: str):
        user = User.query.first_or_404(id)
        return jsonify(user.json())

    @staticmethod
    def update(id: str,data):
        user = User.query.first_or_404(id)
        if endpoint.is_body_data_valide(data,endpoint.body_data_keys):
            for key in list(data.keys()):
                setattr(user, key, data[key])
            try:
                db.session.commit()
                return jsonify(user.json())
            except Exception as e :
                abort(500,e)
        else:
            abort(400,{"Invalid user data"})

    @staticmethod       
    def delete(id):
        user = User.query.first_or_404(id)
        try:
            db.session.delete(user)
            db.session.commit()
            return {"result":"Deleted"}
        except Exception as e : 
            abort(500,e)