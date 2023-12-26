from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    
    #modules 
    
    # User Module
    from app.users.routes.users import users_routes
    # Resource Module
    from app.resource.routes.access import access_routes
    from app.resource.routes.resources import resources_routes
    # Object Module
    from app.object.routes.object import object_routes
    from app.object.routes.file import file_routes
    from app.object.routes.folder import folder_routes
    
    app.register_blueprint(users_routes, url_prefix='/users')
    
    app.register_blueprint(access_routes, url_prefix='/access')
    app.register_blueprint(resources_routes, url_prefix='/resources')
    
    app.register_blueprint(object_routes, url_prefix='/objects')
    app.register_blueprint(file_routes, url_prefix='/files')
    app.register_blueprint(folder_routes, url_prefix='/folders')
    
    @app.route('/endpoint/', methods=['GET'])
    def endpoints():
        return [rule.rule for rule in app.url_map.iter_rules()]

    return app
