from ..models.access import Access as access_model
from app.base.endpoint import endpoint

class Access(endpoint):
    
    def __init__(self ):
        super().__init__(access_model, 'Access', False)
