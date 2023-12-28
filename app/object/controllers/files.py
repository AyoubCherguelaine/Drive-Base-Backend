from app import db
from app.base.endpoint import endpoint
from ..models.file import file

class File(endpoint):
    def __init__(self ):
        super().__init__(file, 'file', True)

