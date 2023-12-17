from flask import Flask, request, jsonify, abort,Blueprint

from ..controllers.users import endpoint

users_routes = Blueprint('user', __name__)

@users_routes.route('/',methods=['GET','POST'])
def users():
    if request.method == 'POST':
        data = request.json
        return endpoint.create_user(data)
    elif request.method == 'GET':
        return endpoint.get_users()
    else:
        abort(404,{"Not Implemented"})


@users_routes.route('/<int:id>', methods=['GET','DELETE', 'PUT'] )
def user(id):
    
    if request.method == 'DELETE':
        return endpoint.delete_user(id)
    elif request.method == 'PUT':
        return endpoint.update_user(id)
    elif request.method == 'GET':
        return endpoint.get_user(id)
    else:
        abort(404,{"Not Implemented"})
