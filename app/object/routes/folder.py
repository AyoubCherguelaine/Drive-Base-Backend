from flask import Flask, request, jsonify, abort,Blueprint
from ..controllers.files import endpoint

folder_routes = Blueprint('folder', __name__)

@folder_routes.route('/',methods=['GET','POST'])
def list_object():
    if request.method == 'POST':
        data = request.json
        return endpoint.create(data)
    elif request.method == 'GET':
        return endpoint.get_list(None)
    
@folder_routes.route('/<int:id>', methods=['GET','DELETE', 'PUT'] )
def access(id):
    if request.method == 'DELETE':
        return endpoint.delete(id)
    elif request.method == 'PUT':
        data = request.json
        return endpoint.update(id,data)
    elif request.method == 'GET':
        return endpoint.get(id)
    else:
        abort(404,{"Not Implemented"})
        
@folder_routes.route('/details/',methods=['GET'])
def list_user_access_details():
    if request.method == 'GET':
        return endpoint.get_list_details(None)
    else:
        abort(404,{"Not Implemented"})
        
@folder_routes.route('<int:id>/details/', methods=['GET'] )
def user_access_details(id):
    if request.method == 'GET':
        return endpoint.get_details(id)
    else:
        abort(404,{"Not Implemented"})