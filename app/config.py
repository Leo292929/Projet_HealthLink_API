import os

class Config:
    """
    Configuration de base qui s'applique à tous les environnements.
    Les sous-classes peuvent surcharger ces valeurs selon les besoins.
    """
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev_secret_key')  # Clé secrète pour la sécurité
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Désactiver le suivi des modifications pour économiser des ressources
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'dev_jwt_secret_key')  # Clé pour la signature des JWT
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # Durée de validité du token d'accès (en secondes)
    CORS_HEADERS = 'Content-Type'  # Définir les en-têtes autorisés pour les requêtes CORS

class DevelopmentConfig(Config):
    """
    Configuration spécifique à l'environnement de développement.
    """
    DEBUG = True  # Activer le mode debug

    # Configuration de la base de données en utilisant les informations fournies
    MYSQL_DB = os.getenv('MYSQL_ADDON_DB', 'bgf47ma31xifvcukugun')
    MYSQL_HOST = os.getenv('MYSQL_ADDON_HOST', 'bgf47ma31xifvcukugun-mysql.services.clever-cloud.com')
    MYSQL_PASSWORD = os.getenv('MYSQL_ADDON_PASSWORD', 'tBcaMLUhSDeIqt3VHiCb')
    MYSQL_PORT = os.getenv('MYSQL_ADDON_PORT', '3306')
    MYSQL_USER = os.getenv('MYSQL_ADDON_USER', 'usrfbvxjxu0j4qsl')

    # Construire l'URI de connexion pour SQLAlchemy
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
    )

    SQLALCHEMY_ECHO = True  # Afficher les requêtes SQL dans la console pour le débogage

# Optionnel : vous pouvez également définir un dictionnaire pour choisir la config selon l'environnement
config_by_name = dict(
    development=DevelopmentConfig,
)

