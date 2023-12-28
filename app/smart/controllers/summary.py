from app.base.endpoint import endpoint
from ..models.summary import summary

class Summary(endpoint):
    
    def __init__(self ):
        super().__init__(summary, 'summary', True)
        
    
