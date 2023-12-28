from ..models.user_access import user_access as user_access_model
from app.base.endpoint import endpoint

class user_access(endpoint):
    
    def __init__(self ):
        super().__init__(user_access_model, 'user_access', False)