from flask import Flask
from flask import render_template

from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # app name
    @app.errorhandler(404)
    
    # inbuilt function which takes error as parameter
    def not_found(e):
    # defining function
        return render_template("404.html")

    # Initialize Flask extensions here

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    @app.route('/edge/')
    def edge_page():
        return '<h1>Bleeding Edge</h1>'

    return app