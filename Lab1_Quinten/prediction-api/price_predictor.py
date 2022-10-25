import json
import os
import logging
import sys
import joblib

import pandas as pd
from flask import jsonify

class PricePredictor:
    def __init__(self):
        self.model = None

    def predict_single_record(self, prediction_input):
        print(prediction_input)
        # Download LR model
        client = storage.client(project=project_id)
        bucket = client.get_bucket(model_repo)
        blob = bucket.blob('lr_model.pk1')
        blob.download_to_filename('/tmp/local_lr_model.pk1')
        # Load RandomForestRegressor model
        model = joblib.load('/tmp/local_lr_model.pk1')
        print(json.dumps(prediction_input))
        df = pd.read_json(json.dumps(prediction_input), orient='records')
        print(df)
        y_pred = model.predict(df)
        print(y_pred[0])
        status = (y_pred[0] > 0.5)
        print(type(status[0]))
        # return the prediction outcome as a json message. 200 is HTTP status code 200, indicating successful completion
        return jsonify({'result': str(status[0])}), 200
