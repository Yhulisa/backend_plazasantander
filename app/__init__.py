from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api
from flask_jwt_extended import JWTManager
from flask_mail import Mail

from app.config import environment


app = Flask(__name__)
# @app.route('/roles',methods=['GET','POST','DELETE','PATCH'])
# def roles():
# if request.method =='POST':
#         return ""
# else:
#     return render_template ('pricing.html')
# if __name__ == '__main__':
# if not os.path.exists(app.config['UPLOAD_FOLDER']):
#     os.makedirs(app.config['UPLOAD_FOLDER'])
# app.run(debug=True, host="0.0.0.0",port=os.getenv("PORT",defaul=5000))

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
