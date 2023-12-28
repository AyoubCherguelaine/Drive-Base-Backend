from flask import Blueprint
from app.base.routes import Routes
from ..controllers.access import Access

Access = Access()

access_routes = Blueprint('access', __name__)

routes = Routes(Access, access_routes, DETAILS=False)