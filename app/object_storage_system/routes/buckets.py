from flask import Blueprint
from ..controllers.buckets import Bucket
from app.base.routes import Routes

Bucket= Bucket()

bucket_routes = Blueprint('bucket',__name__)

routes =  Routes(Bucket,bucket_routes,DETAILS=False)