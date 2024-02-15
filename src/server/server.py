from flask import Flask
from flask_restful import Api

from .routes.upload import Upload

def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(Upload, '/upload')
    return app  