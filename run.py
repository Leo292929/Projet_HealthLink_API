from app import create_app
import os
# Créer l'instance de l'application Flask
app = create_app()

if __name__ == '__main__':
    # Démarrer le serveur Flask en mode debug (ou pas)
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port,debug=True)