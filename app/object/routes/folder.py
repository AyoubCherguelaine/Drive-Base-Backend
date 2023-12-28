from flask import Flask,Blueprint
from ..controllers.folder import Folder
from app.base.routes import Routes

Folder = Folder()
folder_routes = Blueprint('folder', __name__)

routes = Routes(Folder,folder_routes,DETAILS=True)
