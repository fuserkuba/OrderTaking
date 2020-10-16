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

    def get_order_parser(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('order_id', type=str, help='Order ID')
        parser.add_argument('store_id', type=str, help='Store ID of the order')
        parser.add_argument('to_user_distance', type=float, help='Distance (km) between store and user location')
        parser.add_argument('to_user_elevation', type=float, help='Difference (m) between the store and user altitude')
        parser.add_argument('total_earning', type=float, help='Courier earning by delivering the order')
        parser.add_argument('created_at', type=str, help='Timestamp of order creation')
        return parser

    def delete(self):
        orders.clear()
        return "All orders predictions were deleted"

    def get(self):
        return orders

    @marshal_with(resource_fields)
    def post(self):
        # strict=True ensures that an error is thrown if the request includes arguments your parser does not define
        args = self.get_order_parser().parse_args(strict=True)
        # process order
        return self.process(args)

    @marshal_with(resource_fields)
    def put(self):
        root_parser = reqparse.RequestParser()
        root_parser.add_argument('orders', action='append', type=dict)
        root_args = root_parser.parse_args(strict=True)
        processed = [self.process(order) for order in root_args['orders']]
        return processed

    def process(self, order_dict):
        prediction, confidence = self.predict(order_dict)

        order_dict['prediction'] = prediction
        order_dict['confidence'] = confidence

        orders[order_dict['order_id']] = order_dict
        return order_dict

    def predict(self, order):
            return 1, 0.9


api.add_resource(PredictToTakeOrder, '/toTake')

if __name__ == '__main__':
    app.run(debug=True)
