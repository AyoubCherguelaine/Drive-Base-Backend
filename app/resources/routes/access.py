from flask import Flask, request, jsonify, abort,Blueprint

from ..controllers.access import endpoint

access_routes = Blueprint('access', __name__)

@access_routes.route('/',methods=['GET','POST'])
def list_access():
    if request.method == 'POST':
        data = request.json
        return endpoint.create(data)
    elif request.method == 'GET':
        return endpoint.get_list()
    else:
        abort(404,{"Not Implemented"})


@access_routes.route('/<int:id>', methods=['GET','DELETE', 'PUT'] )
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
