from flask import Flask, Blueprint
from app.base.routes import Routes
from ..controllers.users import User

from app.base.endpoint import endpoint

User = User()
users_routes = Blueprint('user', __name__)


class routers(Routes):
    def __init__(self,endpoint,routes,DETAILS=False):
        super().__init__(endpoint,routes,DETAILS)
        self.auth()
    
    def auth(self):
        self.generate_route("login",methods=['POST'],parameter='login',authorize=False)
        self.generate_route("check_token",methods=['GET'],parameter='check',authorize=True)

routes = routers(User,users_routes,DETAILS=False)
