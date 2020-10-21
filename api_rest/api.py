from flask import Flask
from flask_mongoengine import MongoEngine
from flask_restful_swagger_3 import Api, get_swagger_blueprint
from flask_cors import CORS
from resources import PredictToTakeOrder, ConsultToTakeOrder

app = Flask(__name__)
CORS(app)
app.config['MONGODB_SETTINGS'] = {
    "db": "orders",
    "host": "mongodb"
}
db = MongoEngine(app)

api = Api(app)

SWAGGER_URL = '/api/doc'  # URL for exposing Swagger UI (without trailing '/')
API_URL = 'swagger.json'  # Our API url (can of course be a local resource)

swagger_blueprint = get_swagger_blueprint(
    api.open_api_json,
    swagger_prefix_url=SWAGGER_URL,
    swagger_url=API_URL,
    title='Order Taking', version='1')

api.add_resource(PredictToTakeOrder, '/toTake')
api.add_resource(ConsultToTakeOrder, '/toTake/<order_id>')

app.register_blueprint(swagger_blueprint)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
