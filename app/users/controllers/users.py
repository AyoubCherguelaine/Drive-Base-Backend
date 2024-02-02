from app import db
from app.base.endpoint import endpoint
from ..models.users import User as user_model

from flask import request, jsonify, abort

class User(endpoint):
    def __init__(self ):
        super().__init__(user_model, 'file', True)
        
    def login(self):
        data = request.json

        # Guard clause for invalid data
        if not self._is_body_data_valide(data,create=False):
            return abort(404, {"Error": "Data Not Valid"})

        # Use get_or_404 to simplify model retrieval
        model = self.model.get_user_model_by_email(data['email'])
        
        # Check password and generate token
        if model.check_password(data['password']):
            return self._Generate_token(model.id, model.username, model.email)
        else:
            return abort(403, {"Error": "Access Denied"})
        
    def check_token(self):
        try:
            user_data = self._get_user_data()
            return jsonify(user_data)
        except :
            return abort(404)
    