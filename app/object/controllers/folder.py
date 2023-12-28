from app import db
from ..models.folder import folder as folder_model
from app.base.endpoint import endpoint


class Folder(endpoint):
    
    def __init__(self ):
        super().__init__(folder_model, 'folder', True)