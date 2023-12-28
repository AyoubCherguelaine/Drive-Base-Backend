from ..models.user_access import user_access
from app.base.endpoint import endpoint

class user_access(endpoint):
    
    def __init__(self ):
        super().__init__(user_access, 'user_access', False)