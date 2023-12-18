from app import db
from ..models.ressources import Ressource
from flask import request, jsonify, abort

class endpoint:
    
    @staticmethod
    def check_ressource_data(data,create=False)->bool:
        required_keys = {"name","description"}
        if create and set(data.keys()) == required_keys:
            return True
        elif not create and set(data.keys()) & required_keys:
            return True
        else:
            return False

    @staticmethod
    def create_ressource(data):
        if endpoint.check_ressource_data(data, create = True):
            ressource = Ressource(
                name=data['name'],
                description=data['description']
            )
            try:
                db.session.add(ressource)
                db.session.commit()
                return jsonify(ressource)
            except Exception as e:
                abort(500,e.message)
        else:
            abort(400 , {"message": "Invalid ressource data" })
        
    
    @staticmethod
    def get_ressources():
        ressources = Ressource.query.order_by(Ressource.id).all()
        ressource_list = [ressource.json() for ressource in ressources]
        return jsonify(ressource_list)   

    @staticmethod
    def get_ressource(id: str):
        ressource = Ressource.query.first_or_404(id)
        return jsonify(ressource.json())
    
    @staticmethod
    def update_ressource(id: str,data):
        ressource = Ressource.query.first_or_404(id)
        if endpoint.check_ressource_data(data):
            for key in list(data.keys()):
                setattr(ressource, key, data[key])
            try:
                db.session.commit()
                return jsonify(ressource.json())
            except Exception as e :
                abort(500,e.message)
        else:
            abort(400,{"Invalid ressource data"})
            
            
    @staticmethod       
    def delete_ressource(id):
        ressource = Ressource.query.first_or_404(id)
        try:
            db.session.delete(ressource)
            db.session.commit()
            return True
        except Exception as e : 
            abort(500,e.message)