from flask import Flask, Blueprint
from app.base.routes import Routes
from ..controllers.summary import Summary

Summary = Summary()

categories_routes = Blueprint('summary', __name__)

routes = Routes(Summary,categories_routes,DETAILS=False)