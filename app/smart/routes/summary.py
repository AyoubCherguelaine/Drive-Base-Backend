from flask import Flask, Blueprint
from app.base.routes import Routes
from ..controllers.summary import Summary

Summary = Summary()

summary_routes = Blueprint('summary', __name__)

routes = Routes(Summary,summary_routes,DETAILS=True)