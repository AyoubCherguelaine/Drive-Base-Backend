from app.base.endpoint import endpoint
from ..models.model import model

class Model(endpoint):
    
    def __init__(self ):
        super().__init__(model, 'model', False)
        
    
