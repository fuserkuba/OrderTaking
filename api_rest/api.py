from flask import Flask, request
from flask_restful import Api, Resource, reqparse


app = Flask(__name__)
api = Api(app)

orders = {}

class PredictToTakeOrder(Resource):

    def delete(self):
        orders.clear()
        return "All orders predictions were deleted"

    def get(self):
        return orders

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('order_id')
        parser.add_argument('store_id')
        parser.add_argument('to_user_distance')
        parser.add_argument('to_user_elevation')
        parser.add_argument('total_earning')
        parser.add_argument('created_at')

        args = parser.parse_args()

        prediction=1
        confidence=0.9

        args['prediction'] = prediction
        args['confidence'] = confidence

        output = {'order_id': args['order_id'], 'prediction': prediction, 'confidence': confidence}

        orders[args['order_id']] = args

        return output

api.add_resource(PredictToTakeOrder, '/toTake')

if __name__ == '__main__':
    app.run(debug=True)