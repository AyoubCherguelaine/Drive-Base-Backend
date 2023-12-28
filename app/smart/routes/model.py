from flask import Flask, Blueprint
from app.base.routes import Routes
from ..controllers.model import Model

Model = Model()


categories_routes = Blueprint('model', __name__)

routes = Routes(Model,categories_routes,DETAILS=False)