from flask import Flask, Blueprint
from app.base.routes import Routes
from ..controllers.model import Model

Model = Model()


models_routes = Blueprint('model', __name__)

routes = Routes(Model,models_routes,DETAILS=False)