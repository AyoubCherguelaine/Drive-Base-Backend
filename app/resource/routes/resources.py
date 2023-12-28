from flask import Flask, request, jsonify, abort,Blueprint
from app.base.routes import Routes

from ..controllers.resources import Resource 
from ..controllers.user_access import user_access

Resource = Resource()
# user_access = user_access()

resources_routes = Blueprint('resources', __name__)

routes1 = Routes(Resource,resources_routes,DETAILS=False)
# routes2 = Routes(user_access,resources_routes,DETAILS=False, base_route="user")