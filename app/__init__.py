from flask import Flask
from os import getenv
from app.models import db
# from app.apiModels import ma
from app.apiv1 import apiRoutes
from app.api.user import bcrypt
from flask_migrate import Migrate

# Flask Activation
app = Flask(__name__, static_folder='../dist/static')

# Set Configurations
secretKey = getenv('SECRET_KEY')
dbUri = getenv('SQLALCHEMY_DATABASE_URI')
sqlTrackModifcation = getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

# Activate Configurations
app.config['SECRET_KEY'] = secretKey
app.config['SQLALCHEMY_DATABASE_URI'] = dbUri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = sqlTrackModifcation


# Activate Extensions
db.init_app(app)
# ma.init_app(app)
migrate = Migrate(app, db)
bcrypt.init_app(app)

# Activate Blueprints
app.register_blueprint(apiRoutes)

if __name__ == '__main__':
    app.jinja_env.cache = {}
    app.run()
