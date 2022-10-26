import json

import pandas as pd
from flask import jsonify
from keras.models import load_model


class PricePredictor:
    def __init__(self):
        self.model = None

    def predict_single_record(self, prediction_input):
        print(prediction_input)
        model = LinearRegression().fit(x,y) # insert prediction model
        print(json.dumps(prediction_input))
        df = pd.read_json(json.dumps(prediction_input), orient='records')
        print(df)
        y_pred = model.predict(df)
        print(y_pred[0])
        status = (y_pred[0] > 0.5)
        print(type(status[0]))
        # return the prediction outcome as a json message. 200 is HTTP status code 200, indicating successful completion
        return jsonify({'result': str(status[0])}), 200
