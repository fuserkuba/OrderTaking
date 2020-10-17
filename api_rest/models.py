import mongoengine as me


class Order(me.Document):
    order_id = me.StringField(primary_key=True)
    store_id = me.IntField()
    to_user_distance = me.FloatField()
    to_user_elevation = me.FloatField()
    total_earning = me.FloatField()
    created_at=me.StringField(required=True)
    prediction = me.IntField()
    confidence = me.FloatField()
