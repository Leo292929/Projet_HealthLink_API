from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

# Initialisation des extensions sans les attacher à l'application pour le moment
db = SQLAlchemy()            # Pour gérer les opérations liées à la base de données
jwt = JWTManager()           # Pour gérer les tokens JWT
cors = CORS()                # Pour gérer le Cross-Origin Resource Sharing (CORS)
