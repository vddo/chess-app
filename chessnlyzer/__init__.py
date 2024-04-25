from flask import Flask
import os

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(app.instance_path, 'chessnlyzer.sqlite')
    )

    @app.route('/')
    def hello():
        return '<h1>Hello!</h1>'

    return app
