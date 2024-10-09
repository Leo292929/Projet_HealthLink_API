from app import create_app

# Créer l'instance de l'application Flask
app = create_app()

if __name__ == '__main__':
    # Démarrer le serveur Flask en mode debug (ou pas)
    app.run(debug=True)