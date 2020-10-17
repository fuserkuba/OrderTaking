from flask import Flask, Response
from flask_mongoengine import MongoEngine
from flask_restful import Api, Resource, reqparse, fields, marshal_with, abort
from resources import PredictToTakeOrder,ConsultToTakeOrder

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    "db": "orders",
}
db = MongoEngine(app)

api = Api(app)

api.add_resource(PredictToTakeOrder, '/toTake')
api.add_resource(ConsultToTakeOrder, '/toTake/<order_id>')

if __name__ == '__main__':
    app.run(debug=True)
