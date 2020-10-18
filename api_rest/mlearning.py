import joblib
import numpy as np


class Classifier():
    filename ='model.joblib'
    model = joblib.load(filename)

    def predict(self, order):
        x = np.array([order.to_user_distance, order.to_user_elevation,  order.total_earning]).reshape(1, -1)
        print(x)
        y_pred = self.model.predict(x)
        return y_pred
