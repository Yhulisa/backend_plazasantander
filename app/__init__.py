from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_cors import CORS
from app.config import environment


app = Flask(__name__)
CORS(app)
@app.route('/Centros_Comerciales', methods=['GET'])
def obtener_centros_comerciales():
    return jsonify({"message": "API funcionando correctamente"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

authorization = {
    'Bearer': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(
    app,
    title='Plaza Santander',
    version='0.1',
    description='RESTApi de Plaza Santander',
    doc='/swagger-ui',
    authorizations=authorization
)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

jwt = JWTManager(app)
mail = Mail(app)
