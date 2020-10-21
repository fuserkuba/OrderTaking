from flask_restful_swagger_3 import Schema


class OrderTaking(Schema):
    type = 'object'
    properties = {
        'order_id': {
            'type': 'string'
        },
        'store_id': {
            'type': 'string'
        },
        'to_user_distance': {
            'type': 'number',
            'format': 'float',
        },
        'to_user_elevation': {
            'type': 'number',
            'format': 'float',
        },
        'total_earning': {
            'type': 'number',
            'format': 'float',
        },
        'created_at': {
            'type': 'string'
        },
        'prediction': {
            'type': 'integer',
            'format': 'int32',
        },
        'confidence': {
            'type': 'number',
            'format': 'float',
        }
    }


class OrderPrediction(Schema):
    type = 'object'
    properties = {
        'order_id': {
            'type': 'string'
        },
        'prediction': {
            'type': 'integer',
            'format': 'int32',
        },
        'confidence': {
            'type': 'number',
            'format': 'float',
        }
    }