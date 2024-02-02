from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.base.endpoint import endpoint

class Routes:
    def __init__(self, endpoint: endpoint, routes: Blueprint, DETAILS=False, base_route="", authorize=False):
        self.endpoint = endpoint
        self.routes = routes
        self.base_route = base_route
        self.init_endpoints(DETAILS, authorize)

    def init_endpoints(self, DETAILS=False, authorize=False):
        self.generate_route("get_list", methods=["GET"], authorize=authorize)
        self.generate_route("get", methods=["GET"], parameter="<int:id>", authorize=authorize)
        self.generate_route("create", methods=["POST"])
        self.generate_route("update", methods=["PUT"], parameter="<int:id>")
        self.generate_route("delete", methods=["DELETE"], parameter="<int:id>")

        if DETAILS:
            self.generate_route("get_list_details", methods=["GET"], subroute="/details/")
            self.generate_route("get_details", methods=["GET"], parameter="<int:id>", subroute="/details/")

    def generate_route(self, action, methods, parameter=None, subroute="", authorize=False):
        function_name = f"{action}_{self.endpoint.model_name}"
        route_path = f'{self.base_route}/{subroute}' if subroute else f'{self.base_route}/'

        endpoint_function = endpoint.get_endpoint(self.endpoint, function_name)
        if authorize:
            endpoint_function = jwt_required()(endpoint_function)

        if parameter:
            route_path += f'/{parameter}'
            
        self.routes.route(route_path, methods=methods)(endpoint_function)
