from flask_sqlalchemy import SQLAlchemy
from app.extensions import db
from .extensions import db
from sqlalchemy import text

def init_db(app):
    """
    Initialise la base de données avec l'application Flask.
    Cette fonction attache SQLAlchemy à l'application Flask, si ce n'est pas déjà fait.
    """
    # Attacher SQLAlchemy à l'application si ce n'est pas déjà fait
    #if not hasattr(app, 'db_initialized'):
    #    db.init_app(app)
    #    app.db_initialized = True  # Marque l'app comme initialisée pour éviter les appels multiples

    # Vérification de la connexion à la base de données sans ré-attacher SQLAlchemy
    test_db_connection(app)


def test_db_connection(app):
    with app.app_context():
        try:
            # Créer une connexion à partir de l'engine
            with db.engine.connect() as connection:
                # Exécuter une requête de test en utilisant `text` pour le SQL brut
                connection.execute(text('SELECT id FROM user'))
            print("Connexion réussie à la base de données.")
        except Exception as e:
            print(f"Erreur lors de la connexion à la base de données : {e}")