from flask import Flask, request, jsonify, abort,Blueprint

from ..controllers.users import endpoint


users_routes = Blueprint('user', __name__)

@users_routes.route('/',methods=['GET','POST'])
def users():
    if request.method == 'POST':
        data = request.json
        return endpoint.create(data)
    elif request.method == 'GET':
        return endpoint.get_list(None)
    else:
        abort(404,{"Not Implemented"})


@users_routes.route('/<int:id>', methods=['GET','DELETE', 'PUT'] )
def user(id):
    
    if request.method == 'DELETE':
        return endpoint.delete(id)
    elif request.method == 'PUT':
        data = request.json
        return endpoint.update(id,data)
    elif request.method == 'GET':
        return endpoint.get(id)
    else:
        abort(404,{"Not Implemented"})
