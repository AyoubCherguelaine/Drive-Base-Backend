from ..models.access import Access
from app.base.endpoint import endpoint

class Access(endpoint):
    
    def __init__(self ):
        super().__init__(Access, 'Access', False)
