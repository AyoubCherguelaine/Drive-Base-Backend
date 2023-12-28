from flask import Blueprint
from ..controllers.files import File
from app.base.routes import Routes

File = File()

file_routes = Blueprint('file', __name__)

routes = Routes(File,file_routes,DETAILS=True)
