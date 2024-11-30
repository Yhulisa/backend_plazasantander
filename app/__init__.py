from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask import Flask
from flask_cors import CORS
from app.config import environment


app = Flask(__name__)
CORS(app)
@app.route("/")
def helloWorld():
  return "Hello, cross-origin-world!"
app.config.from_object(environment)

authorization = {
    'Bearer': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(
    app,
    title='Boilerplate Flask',
    version='0.1',
    description='RESTApi del Boilerplate',
    doc='/swagger-ui',
    authorizations=authorization
)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

jwt = JWTManager(app)
mail = Mail(app)
