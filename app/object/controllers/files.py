from app import db
from app.base.endpoint import endpoint
from ..models.file import file as file_model

class File(endpoint):
    def __init__(self ):
        super().__init__(file_model, 'file', True)

