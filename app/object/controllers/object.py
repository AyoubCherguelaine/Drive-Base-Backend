from ..models.object import object
from app.base.endpoint import endpoint

class Object(endpoint):
    
    def __init__(self):
        super().__init__(object, 'object', True)