from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    
    #modules 
    from app.users.routes.users import users_routes
    from app.resource.routes.access import access_routes
    from app.resource.routes.resources import resources_routes
    
    
    app.register_blueprint(users_routes, url_prefix='/users')
    app.register_blueprint(access_routes, url_prefix='/access')
    app.register_blueprint(resources_routes, url_prefix='/resources')
    
    @app.route('/endpoint/', methods=['GET'])
    def endpoints():
        return [rule.rule for rule in app.url_map.iter_rules()]

    return app
