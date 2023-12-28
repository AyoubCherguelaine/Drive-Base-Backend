
from ..models.resources import resource 
from app.base.endpoint import endpoint

class Resource(endpoint):
    
    def __init__(self ):
        super().__init__(resource, 'resource', False)
