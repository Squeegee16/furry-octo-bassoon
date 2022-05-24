from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from webif.config import Config


db = SQLAlchemy()

def rover_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    # db.init_app(app)

    from webif.main.main import main
    from webif.errors.handlers import errors

    app.register_blueprint(main)#, url_prefix='/')
    app.register_blueprint(errors)#, url_prefix='/')

#    from webif.models import User, Note
#    create_database(app)

    return app

def create_database(app):
    if not path.exists('website/' + 'database.db'):
        db.create_all(app=app)
        print('Created Database!')


#https://www.youtube.com/watch?v=dam0GPOAvVI

