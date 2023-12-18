from flask import Flask, request, jsonify, abort,Blueprint

from ..controllers.ressources import endpoint as ress_endpoint
from ..controllers.user_access import endpoint as ua_endpoint

ressources_routes = Blueprint('ressources', __name__)

@ressources_routes.route('/',methods=['GET','POST'])
def ressources():
    if request.method == 'POST':
        data = request.json
        return ress_endpoint.create_ressource(data)
    elif request.method == 'GET':
        return ress_endpoint.get_ressources()
    else:
        abort(404,{"Not Implemented"})


@ressources_routes.route('/<int:id>', methods=['GET','DELETE', 'PUT'] )
def ressource(id):
    
    if request.method == 'DELETE':
        return ress_endpoint.delete_ressource(id)
    elif request.method == 'PUT':
        data = request.json
        return ress_endpoint.update_ressource(id,data)
    elif request.method == 'GET':
        return ress_endpoint.get_ressource(id)
    else:
        abort(404,{"Not Implemented"})
        
        
@ressources_routes.route('/<int:id>/user',methods=['GET','POST'])
def list_user_access():
    if request.method == 'POST':
        data = request.json
        return ua_endpoint.create_user_access(data)
    elif request.method == 'GET':
        return ua_endpoint.get_list_user_access()
    else:
        abort(404,{"Not Implemented"})


@ressources_routes.route('/<int:id>/user/<int:id_user>', methods=['GET','DELETE', 'PUT'] )
def user_access(id):
    
    if request.method == 'DELETE':
        return ua_endpoint.delete_user_access(id)
    elif request.method == 'PUT':
        data = request.json
        return ua_endpoint.update_user_access(id,data)
    elif request.method == 'GET':
        return ua_endpoint.get_user_access(id)
    else:
        abort(404,{"Not Implemented"})
