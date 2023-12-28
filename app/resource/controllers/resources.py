
from ..models.resources import resource as resource_model
from app.base.endpoint import endpoint

class Resource(endpoint):
    
    def __init__(self ):
        super().__init__(resource_model, 'resource', False)
