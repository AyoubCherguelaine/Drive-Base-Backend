from app import db
from ..models.users import User
from flask import request, jsonify, abort

class endpoint:
    @staticmethod
    def check_user_data(data, create=False)->bool:
        required_keys = {'firstname', 'lastname', 'username', 'email', 'password'}
        if create and set(data.keys()) == required_keys:
            return True
        elif not create and set(data.keys()) & required_keys:
            return True
        else:
            return False
        
    @staticmethod
    def create_user(data):
        if endpoint.check_user_data(data, create=True):
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
    def get_users():
        users = User.query.order_by(User.id).all()
        users_list = [user.json() for user in users]
        return jsonify(users_list)

    @staticmethod
    def get_user(id: str):
        user = User.query.first_or_404(id)
        return jsonify(user.json())

    @staticmethod
    def update_user(id: str,data):
        user = User.query.first_or_404(id)
        if endpoint.check_user_data(data):
            for key in list(data.keys()):
                setattr(user, key, data[key])
            try:
                db.session.commit()
                return jsonify(user.json())
            except Exception as e :
                abort(500,e.message)
        else:
            abort(400,{"Invalid user data"})

    @staticmethod       
    def delete_user(id):
        user = User.query.first_or_404(id)
        try:
            db.session.delete(user)
            db.session.commit()
            return {"result":True}
        except Exception as e : 
            abort(500,e.message)