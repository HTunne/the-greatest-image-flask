from flask import Flask
from flask_cors import CORS
from flask_restful import Api

#from the_greatest_image_flask.config import ProductionConfig, DevelopmentConfig
from the_greatest_image_flask.resources import ImageResource

def create_app():
    app = Flask(__name__, instance_relative_config = True)
    # if app.config["ENV"] == "production":
    #     app.config.from_object(ProductionConfig())
    # else:
    #     app.config.from_object(DevelopmentConfig())

    CORS(app)

    api = Api(app)
    api.add_resource(ImageResource, '/')
    
    return app
