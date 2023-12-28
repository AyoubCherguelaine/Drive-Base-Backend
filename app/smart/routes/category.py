from flask import Flask, Blueprint
from app.base.routes import Routes
from ..controllers.category import Category

Category = Category()

categories_routes = Blueprint('category', __name__)

routes = Routes(Category,categories_routes,DETAILS=True)