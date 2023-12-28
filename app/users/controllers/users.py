from app import db
from app.base.endpoint import endpoint
from ..models.users import User

class User(endpoint):
    def __init__(self ):
        super().__init__(User, 'file', True)
