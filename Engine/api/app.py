import os
from datetime import timedelta
from flask_cors import CORS
from flask import Flask
from flask_restful import Api
from flasgger import Swagger, swag_from
from flask_session import Session
from flask_jwt_extended import JWTManager

from api.config import env_config

api = Api()

def create_app(config_name):
    """This is used to set the app and swagger configurations  and the requirements"""
    
    template = {
        "swagger": "2.0",
        "info": {
            "title" : "Flask Tutorial",
            "description": "Swagger tutorial",
            "version": "1.0.0"

        },
        "securityDefinitions": {"APIKeyHeader": {"type": "apiKey", "name":"Authorization",
                                "in": "header"}}
    }
    
    app = Flask(__name__)

    app.config['SWAGGER'] = {
        'title': 'Flask Tutorial',
        'uiversion': 3, # Related to swagger
        'specs_route':"/swagger/"
    }
    # Session nare temporary files stored about the user. This is done on the users side.
    app.config['SESSION_PERMANENT'] = False
    app.config['SESSION_TYPE'] = "filesystem"
    app.config['SESSION_FILE_DIR'] = '../../flask_session' #to create a session folder
    app.config['JSON_SORT_KEYS'] = False # to sort the keys in ascending order automatically

    app.config.from_object(env_config[os.getenv("FLASK_ENV")])
    Session(app) # Its a unique identifier attached to Log calling of end points, like an authetifiaction request sent to a user
    jwt = JWTManager(app) # the authenitification 
    api.init_app(app) # creates an instance of the particular package

    CORS(app) # transfer the data from react to java, if the fron end is python no need for cors
    Swagger(app, template=template) # defines the template for swagger

    return app
