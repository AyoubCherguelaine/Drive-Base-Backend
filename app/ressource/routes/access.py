from flask import Flask, request, jsonify, abort,Blueprint

from ..controllers.access import endpoint

access_routes = Blueprint('access', __name__)

@access_routes.route('/',methods=['GET','POST'])
def list_access():
    if request.method == 'POST':
        data = request.json
        return endpoint.create_access(data)
    elif request.method == 'GET':
        return endpoint.get_list_access()
    else:
        abort(404,{"Not Implemented"})


@access_routes.route('/<int:id>', methods=['GET','DELETE', 'PUT'] )
def access(id):
    
    if request.method == 'DELETE':
        return endpoint.delete_access(id)
    elif request.method == 'PUT':
        data = request.json
        return endpoint.update_access(id,data)
    elif request.method == 'GET':
        return endpoint.get_access(id)
    else:
        abort(404,{"Not Implemented"})
