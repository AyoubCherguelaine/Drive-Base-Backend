from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_jwt_extended import JWTManager

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    # Set the secret key to something unique to your application
    app.config['JWT_SECRET_KEY'] = 'your-secret-key'

    jwt = JWTManager(app)
    #modules 
    
    # User Module
    from app.users.routes.users import users_routes
    # Resource Module
    from app.resource.routes.access import access_routes
    from app.resource.routes.resources import resources_routes
    from app.resource.routes.user_access import user_access_routes
    # Object Module
    from app.object.routes.object import object_routes
    from app.object.routes.file import file_routes
    from app.object.routes.folder import folder_routes
    # Smart Module
    from app.smart.routes.category import categories_routes
    from app.smart.routes.model import models_routes
    from app.smart.routes.summary import summary_routes
    # object storage
    from app.object_storage_system.routes.buckets import bucket_routes
    
    app.register_blueprint(users_routes, url_prefix='/users')
    
    app.register_blueprint(access_routes, url_prefix='/access')
    app.register_blueprint(resources_routes, url_prefix='/resources')
    app.register_blueprint(user_access_routes, url_prefix='/resources/user')

    
    app.register_blueprint(object_routes, url_prefix='/objects')
    app.register_blueprint(file_routes, url_prefix='/files')
    app.register_blueprint(folder_routes, url_prefix='/folders')
        
    app.register_blueprint(categories_routes, url_prefix='/categories')
    app.register_blueprint(models_routes, url_prefix='/models')
    app.register_blueprint(summary_routes, url_prefix='/summaries')
    
    app.register_blueprint(bucket_routes,url_prefix='/buckets')
    
    @app.route('/endpoint/', methods=['GET'])
    def endpoints():
        endpoints = [{"endpoint": rule.rule, "methods": [method for method in rule.methods if method in ['POST', 'GET', 'DELETE', 'PUT']]} for rule in app.url_map.iter_rules()]
        return endpoints

    return app
