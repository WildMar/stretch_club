from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask import Flask
from flask_apispec import FlaskApiSpec
from flask_cors import CORS
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy

# initialize app and api instances
app = Flask(__name__)
api = Api(app)

# Setup configurations for using flaskapispec
app.config['APISPEC_SPEC'] = APISpec(
    title="stretch_club",
    version="v1.0",
    openapi_version="3.0.2",
    plugins=[MarshmallowPlugin()]
)
app.config["APISPEC_SWAGGER_URL"] = "/swagger/"

# Configurations for sqlalchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///stretch_club.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

# Register extensions
docs = FlaskApiSpec()
cors = CORS()
db = SQLAlchemy()


def register_extensions():
    db.init_app(app=app)
    cors.init_app(app=app)
    docs.init_app(app=app)


if __name__ == "__main__":
    register_extensions()
    app.run(debug=True)
