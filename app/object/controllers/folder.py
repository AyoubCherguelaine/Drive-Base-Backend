from app import db
from ..models.folder import folder
from app.base.endpoint import endpoint


class Folder(endpoint):
    
    def __init__(self ):
        super().__init__(folder, 'folder', True)