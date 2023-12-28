from ..models.object import object as object_model
from app.base.endpoint import endpoint

class Object(endpoint):
    
    def __init__(self):
        super().__init__(object_model, 'object', True)