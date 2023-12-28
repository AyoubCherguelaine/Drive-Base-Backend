from flask import Flask, request, jsonify, abort,Blueprint
from app.base.routes import Routes

from ..controllers.user_access import user_access

user_access = user_access()

user_access_routes = Blueprint('user_access', __name__)

routes1 = Routes(user_access,user_access_routes,DETAILS=False)