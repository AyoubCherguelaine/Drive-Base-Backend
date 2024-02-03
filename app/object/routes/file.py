from flask import Blueprint

from app.base.endpoint import endpoint
from ..controllers.files import File
from app.base.routes import Routes

File = File()

file_routes = Blueprint('file', __name__)


class routes(Routes):
    
    def __init__(self, endpoint: endpoint, routes: Blueprint, DETAILS=False, base_route="", authorize=False):
        super().__init__(endpoint, routes, DETAILS=DETAILS, base_route=base_route, authorize=authorize)
    
routes = routes(File,file_routes,DETAILS=True, authorize=True)
