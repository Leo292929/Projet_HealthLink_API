from flask import Flask
from .config import DevelopmentConfig
from .extensions import db, jwt, cors
from .db import init_db
from .extensions import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)



    # Initialiser les extensions avec l'application Flask
    db.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)

    init_db(app)

    # Importer et enregistrer les routes (blueprints)
    from .api.views import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app






