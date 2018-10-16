from flask import Flask, current_app, send_file
from os import getenv, path
from app.models import db
# from app.apiModels import ma
from app.apiv1 import apiRoutes
from app.api.restful.user import bcrypt
from flask_migrate import Migrate

# Flask Activation
app = Flask(__name__, static_folder='../dist/static')

# Set Configurations
secretKey = getenv('SECRET_KEY')
dbUri = getenv('DATABASE_URI')
sqlTrackModifcation = getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
app_dir = path.dirname(__file__)
root_dir = path.dirname(app_dir)
dist_dir = path.join(root_dir, 'dist')

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


@app.route('/')
def index_client():
    dist_dir = current_app
    entry = path.join(dist_dir, 'index.html')
    return send_file(entry)


if __name__ == '__main__':
    app.jinja_env.cache = {}
    app.run()
