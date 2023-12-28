from flask import Flask,Blueprint
from ..controllers.object import Object
from app.base.routes import Routes

Object = Object()

object_routes = Blueprint('object', __name__)

routes = Routes(Object,object_routes,DETAILS=True)
