from flask import Flask, Blueprint
from app.base.routes import Routes
from ..controllers.users import User

User = User()
users_routes = Blueprint('user', __name__)

routes = Routes(User,users_routes,DETAILS=False)
