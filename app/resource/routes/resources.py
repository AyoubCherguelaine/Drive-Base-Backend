from flask import Flask, request, jsonify, abort,Blueprint

from ..controllers.resources import endpoint as ress_endpoint
from ..controllers.user_access import endpoint as ua_endpoint

resources_routes = Blueprint('resources', __name__)

@resources_routes.route('/',methods=['GET','POST'])
def resources():
    if request.method == 'POST':
        data = request.json
        return ress_endpoint.create(data)
    elif request.method == 'GET':
        return ress_endpoint.get_list()
    else:
        abort(404,{"Not Implemented"})


@resources_routes.route('/<int:id>', methods=['GET','DELETE', 'PUT'] )
def resource(id):
    if request.method == 'DELETE':
        return ress_endpoint.delete(id)
    elif request.method == 'PUT':
        data = request.json
        return ress_endpoint.update(id,data)
    elif request.method == 'GET':
        return ress_endpoint.get(id)
    else:
        abort(404,{"Not Implemented"})
        


@resources_routes.route('/user/',methods=['GET','POST'])
def list_user_access():
    if request.method == 'POST':
        data = request.json
        return ua_endpoint.create(data)
    elif request.method == 'GET':
        return ua_endpoint.get_list(None)
    else:
        abort(404,{"Not Implemented"})
        
@resources_routes.route('/user/details/',methods=['GET','POST'])
def list_user_access_details():
    if request.method == 'GET':
        return ua_endpoint.get_list_details(None)
    else:
        abort(404,{"Not Implemented"})
    
@resources_routes.route('/user/<int:id_user>/details/', methods=['GET','DELETE', 'PUT'] )
def user_access_details(id_user):
    if request.method == 'GET':
        return ua_endpoint.get_details(id_user)
    else:
        abort(404,{"Not Implemented"})
        
@resources_routes.route('/user/<int:id_user>', methods=['GET','DELETE', 'PUT'] )
def user_access(id_user):
    if request.method == 'DELETE':
        return ua_endpoint.delete(id_user)
    elif request.method == 'PUT':
        data = request.json
        return ua_endpoint.update(id_user,data)
    elif request.method == 'GET':
        return ua_endpoint.get(id_user)
    else:
        abort(404,{"Not Implemented"})
        
@resources_routes.route('/<int:id>/user/',methods=['GET','POST'])
def list_user_access_by_resource(id):
    if request.method == 'POST':
        data = request.json
        return ua_endpoint.create(data)
    elif request.method == 'GET':
        return ua_endpoint.get_list()
    else:
        abort(404,{"Not Implemented"})


@resources_routes.route('/<int:id>/user/<int:id_user>', methods=['GET','DELETE', 'PUT'] )
def user_access_by_resource(id,id_user):
    
    if request.method == 'DELETE':
        return ua_endpoint.delete(id)
    elif request.method == 'PUT':
        data = request.json
        return ua_endpoint.update(id,data)
    elif request.method == 'GET':
        return ua_endpoint.get(id)
    else:
        abort(404,{"Not Implemented"})
