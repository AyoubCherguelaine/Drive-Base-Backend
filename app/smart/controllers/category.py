from app.base.endpoint import endpoint
from ..models.category import category as category_model

class Category(endpoint):
    
    def __init__(self ):
        super().__init__(category_model, 'category', True)
        
    
