from flask import Flask, request, jsonify, abort,Blueprint

from ..controllers.ressources import endpoint as ress_endpoint
from ..controllers.user_access import endpoint as ua_endpoint

ressources_routes = Blueprint('ressources', __name__)

@ressources_routes.route('/',methods=['GET','POST'])
def ressources():
    if request.method == 'POST':
        data = request.json
        return ress_endpoint.create(data)
    elif request.method == 'GET':
        return ress_endpoint.get_list()
    else:
        abort(404,{"Not Implemented"})


@ressources_routes.route('/<int:id>', methods=['GET','DELETE', 'PUT'] )
def ressource(id):
    
    if request.method == 'DELETE':
        return ress_endpoint.delete(id)
    elif request.method == 'PUT':
        data = request.json
        return ress_endpoint.update(id,data)
    elif request.method == 'GET':
        return ress_endpoint.get(id)
    else:
        abort(404,{"Not Implemented"})
        


@ressources_routes.route('/user/',methods=['GET','POST'])
def list_user_access():
    if request.method == 'POST':
        data = request.json
        return ua_endpoint.create(data)
    elif request.method == 'GET':
        return ua_endpoint.get_list()
    else:
        abort(404,{"Not Implemented"})
        
        
@ressources_routes.route('/user/<int:id_user>', methods=['GET','DELETE', 'PUT'] )
def user_access(id_user):
    
    if request.method == 'DELETE':
        return ua_endpoint.delete(id_user)
    elif request.method == 'PUT':
        data = request.json
        return ua_endpoint.update(id_user,data)
    elif request.method == 'GET':
        return ua_endpoint.get(id)
    else:
        abort(404,{"Not Implemented"})
        
        
@ressources_routes.route('/<int:id>/user/',methods=['GET','POST'])
def list_user_access_by_ressource(id):
    if request.method == 'POST':
        data = request.json
        return ua_endpoint.create(data)
    elif request.method == 'GET':
        return ua_endpoint.get_list()
    else:
        abort(404,{"Not Implemented"})


@ressources_routes.route('/<int:id>/user/<int:id_user>', methods=['GET','DELETE', 'PUT'] )
def user_access_by_ressource(id,id_user):
    
    if request.method == 'DELETE':
        return ua_endpoint.delete(id)
    elif request.method == 'PUT':
        data = request.json
        return ua_endpoint.update(id,data)
    elif request.method == 'GET':
        return ua_endpoint.get(id)
    else:
        abort(404,{"Not Implemented"})
