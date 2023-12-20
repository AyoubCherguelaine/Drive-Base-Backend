from app import db
from ..models.ressources import Ressource
from flask import request, jsonify, abort
from app.base.endpoint import endpoint

class endpoint(endpoint):
    body_data_keys= {"name","description"}

    @staticmethod
    def create(data):
        if endpoint.is_body_data_valide(data, create = True):
            ressource = Ressource(
                name=data['name'],
                description=data['description']
            )
            try:
                db.session.add(ressource)
                db.session.commit()
                return jsonify(ressource.json())
            except Exception as e:
                abort(500,e)
        else:
            abort(400 , {"message": "Invalid ressource data" })
        
    
    @staticmethod
    def get_list(query):
        ressources = Ressource.query.order_by(Ressource.id).all()
        ressource_list = [ressource.json() for ressource in ressources]
        return jsonify(ressource_list)   

    @staticmethod
    def get(id: str):
        ressource = Ressource.query.first_or_404(id)
        return jsonify(ressource.json())
    
    @staticmethod
    def update(id: str,data):
        ressource = Ressource.query.first_or_404(id)
        if endpoint.is_body_data_valide(data):
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
    def delete(id):
        ressource = Ressource.query.first_or_404(id)
        try:
            db.session.delete(ressource)
            db.session.commit()
            return {"result":"Deleted"}
        except Exception as e : 
            abort(500,e.message)