from app import db
from app.base.endpoint import endpoint
from ..models.users import User as user_model

class User(endpoint):
    def __init__(self ):
        super().__init__(user_model, 'file', True)
