from flask import Flask
import os

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(app.instance_path, 'chessnlyzer.sqlite')
    )

    # Ensure an instance directory exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def hello():
        return '<h1>Hello!</h1>'

    # Register init-db, close-db at the end of factory func (before return app)
    from . import db
    db.init_app(app)

    return app

