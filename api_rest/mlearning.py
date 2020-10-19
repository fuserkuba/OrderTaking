import joblib
import numpy as np
import dateutil.parser
from datetime import timedelta

class Classifier():
    filename ='model.joblib'
    model = joblib.load(filename)

    def predict(self, order):
        created = dateutil.parser.parse(order.created_at)
        week_day = created.weekday()
        day = created.day
        hour = created.hour
        working_time = (created - timedelta(hours=8)).hour * 60 + created.minute
        x = np.array([order.to_user_distance,
                      order.to_user_elevation,
                      order.total_earning,
                      week_day,
                      day,
                      hour,
                      working_time
                      ])\
            .reshape(1, -1)
        print("Features in order {} : {}".format(order.order_id, x))
        y_pred = self.model.predict(x)
        prob = self.model.predict_proba(x)
        print("Predict proba:", prob)
        return y_pred[0], prob[0][y_pred[0]]
