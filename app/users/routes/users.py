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
        get_list_function = endpoint.get_endpoint(self.endpoint,f"login_{self.endpoint.model_name}")
        self.routes.route(f'{self.base_route}/login',methods=["POST"])(get_list_function)
        
routes = routers(User,users_routes,DETAILS=False)
