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
        if not self.__is_body_data_valide(data):
            return abort(404, {"Error": "Data Not Valid"})

        # Use get_or_404 to simplify model retrieval
        model = self.model.query.get_or_404(data.email)

        # Check password and generate token
        if model.check_password(data.password):
            return self.__Generate_token(model.id, model.username, model.email)
        else:
            return abort(403, {"Error": "Access Denied"})