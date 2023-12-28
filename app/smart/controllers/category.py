from app.base.endpoint import endpoint
from ..models.category import category

class Category(endpoint):
    
    def __init__(self ):
        super().__init__(category, 'category', False)
        
    
