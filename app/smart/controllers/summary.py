from app.base.endpoint import endpoint
from ..models.summary import summary as summary_model

class Summary(endpoint):
    
    def __init__(self ):
        super().__init__(summary_model, 'summary', True)
        
    
