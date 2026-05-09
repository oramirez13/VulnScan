from flask import Flask


def create_app():
    # Creamos la aplicacion principal de Flask.
    app = Flask(__name__)

    # Importamos el blueprint con las rutas principales del proyecto.
    from app.routes import bp

    # Registramos el blueprint para que Flask conozca todas las vistas.
    app.register_blueprint(bp)

    # Devolvemos la aplicacion ya configurada.
    return app
