from flask_restful import reqparse, fields, marshal_with, abort
from flask_restful_swagger_3 import swagger, Resource
from models import Order
from mlearning import Classifier
from schemas import OrderTaking, OrderPrediction

prediction_fields = {
    'order_id': fields.String,
    'prediction': fields.Integer,
    'confidence': fields.Float
}

order_fields = {
    'order_id': fields.String(attribute='_id'),
    'store_id': fields.String,
    'to_user_distance': fields.Float,
    'to_user_elevation': fields.Float,
    'total_earning': fields.Float,
    'created_at': fields.String,
    'prediction': fields.Integer,
    'confidence': fields.Float
}


class PredictToTakeOrder(Resource):
    classifier = Classifier()

    parser = reqparse.RequestParser(bundle_errors=True)
    parser.add_argument('order_id', type=str, help='Order ID', required=True)
    parser.add_argument('store_id', type=str, help='Store ID of the order', required=True)
    parser.add_argument('to_user_distance', type=float, help='Distance (km) between store and user location',
                        required=True)
    parser.add_argument('to_user_elevation', type=float, help='Difference (m) between the store and user altitude',
                        required=True)
    parser.add_argument('total_earning', type=float, help='Courier earning by delivering the order', required=True)
    parser.add_argument('created_at', type=str, help='Timestamp of order creation', required=True)

    @swagger.tags(['predict'])
    @swagger.reorder_with(OrderTaking, description="Remove all orders taking predictions")
    def delete(self):
        Order.objects.delete()
        return "All orders predictions were deleted"

    @swagger.tags(['predict'])
    @swagger.reorder_list_with(OrderTaking, description="Obtains all orders taking predictions")
    @marshal_with(order_fields)
    def get(self):
        orders = Order.objects
        if not orders:
            abort(404, message="There are not orders")
        return [order.to_mongo() for order in orders]

    @swagger.tags(['predict'])
    @swagger.reorder_with(OrderPrediction, description="Predicts an order taking")
    @swagger.reqparser(name='Order', parser=parser)
    @marshal_with(prediction_fields)
    def post(self):
        # strict=True ensures that an error is thrown if the request includes arguments your parser does not define
        args = self.parser.parse_args(strict=True)
        # process order
        return self.process(args)

    @swagger.tags(['predict'])
    @swagger.reorder_list_with(OrderPrediction,
                               description="Predicts orders taking on batch. "
                                           "The request body must contains a json array of Order")
    @swagger.reqparser(name='Order', parser=parser)
    @marshal_with(prediction_fields)
    def put(self):
        root_parser = reqparse.RequestParser()
        root_parser.add_argument('orders', action='append', type=dict)
        root_args = root_parser.parse_args(strict=True)
        processed = []
        for order in root_args['orders']:
            fake_request = FakeRequest()
            setattr(fake_request, 'json', order)
            setattr(fake_request, 'unparsed_arguments', {})
            args = self.parser.parse_args(req=fake_request, strict=True)
            processed.append(self.process(args))
        return processed

    def process(self, order_dict):
        prediction, confidence = self.classifier.predict(order_dict)
        order_dict['prediction'] = prediction
        order_dict['confidence'] = confidence

        print(order_dict)
        order = Order(**order_dict)
        order.save()

        return order


class FakeRequest(dict):
    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)


class ConsultToTakeOrder(Resource):
    @swagger.tags(['order'])
    @swagger.reorder_with(OrderTaking, description="Returns an order")
    @swagger.response(response_code=404, description="The required order doesn't exist")
    @marshal_with(order_fields)
    def get(self, order_id):
        order = Order.objects(order_id=order_id).first()
        if order is None:
            abort(404, message="Order {} doesn't exist".format(order_id))
        return order.to_mongo()
