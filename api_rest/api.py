from flask import Flask, request
from flask_restful import Api, Resource, reqparse, fields, marshal_with

app = Flask(__name__)
api = Api(app)

orders = {}

resource_fields = {
    'order_id':   fields.String,
    'prediction':   fields.Integer,
    'confidence':   fields.Float
}


class PredictToTakeOrder(Resource):

    def delete(self):
        orders.clear()
        return "All orders predictions were deleted"

    def get(self):
        return orders

    @marshal_with(resource_fields)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('order_id', type=str, help='Order ID')
        parser.add_argument('store_id', type=str, help='Store ID of the order')
        parser.add_argument('to_user_distance', type=float, help='Distance (km) between store and user location')
        parser.add_argument('to_user_elevation', type=float, help='Difference (m) between the store and user altitude')
        parser.add_argument('total_earning', type=float, help='Courier earning by delivering the order')
        parser.add_argument('created_at', type=str, help='Timestamp of order creation')

        # strict=True ensures that an error is thrown if the request includes arguments your parser does not define
        args = parser.parse_args(strict=True)

        prediction = 1
        confidence = 0.9

        args['prediction'] = prediction
        args['confidence'] = confidence

        orders[args['order_id']] = args

        return args


api.add_resource(PredictToTakeOrder, '/toTake')

if __name__ == '__main__':
    app.run(debug=True)
