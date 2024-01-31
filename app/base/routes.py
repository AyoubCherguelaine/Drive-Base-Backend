from flask import Flask, request, jsonify, abort,Blueprint
from app.base.endpoint import endpoint

class Routes:
    
    
    
    def __init__(self, endpoint:endpoint , routes:Blueprint, DETAILS=False, base_route=""):
        self.endpoint = endpoint
        self.routes = routes
        self.base_route = base_route
        self.generate_routes_getter()
        self.generate_routes_post()
        self.generate_routes_put()
        self.generate_routes_delete()
        if DETAILS:
            self.generate_route_details()
        
    def generate_routes_getter(self):  # sourcery skip: extract-duplicate-method
        
        get_list_function = endpoint.get_endpoint(self.endpoint,f"get_list_{self.endpoint.model_name}")
        self.routes.route(f'{self.base_route}/',methods=["GET"])(get_list_function)
        
        get_function = endpoint.get_endpoint(self.endpoint,f"get_{self.endpoint.model_name}")
        self.routes.route(f'{self.base_route}/<int:id>',methods=["GET"])(get_function)

        
    
    def generate_routes_post(self):
        
        create_function = endpoint.get_endpoint(self.endpoint,f"create_{self.endpoint.model_name}")
        self.routes.route(f'{self.base_route}/',methods=["POST"])(create_function)
        
    def generate_routes_put(self):
        
        update_function = endpoint.get_endpoint(self.endpoint,f"update_{self.endpoint.model_name}")
        self.routes.route(f'{self.base_route}/<int:id>',methods=["PUT"])(update_function)
 
    
    def generate_routes_delete(self):
        
        delete_function = endpoint.get_endpoint(self.endpoint,f"delete_{self.endpoint.model_name}") 
        self.routes.route(f'{self.base_route}/<int:id>',methods=["DELETE"])(delete_function)

    
    def generate_route_details(self):
        
        get_list_details_function = endpoint.get_endpoint(self.endpoint,f"get_list_details_{self.endpoint.model_name}")
        self.routes.route(f'{self.base_route}/details/',methods=["GET"])(get_list_details_function)
        
        get_details_function = endpoint.get_endpoint(self.endpoint,f"get_details_{self.endpoint.model_name}")
        self.routes.route(f'{self.base_route}/<int:id>/details/',methods=["GET"])(get_details_function)
        