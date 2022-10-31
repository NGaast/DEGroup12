import json
import os
import logging
import sys
import joblib
import pandas as pd
from flask import jsonify
from google.cloud import storage
import sys


class PricePredictor:
    def __init__(self):
        self.model = None

    def predict_single_record(self, prediction_input):
        print(prediction_input)
        # Download LR model
        project_id = os.environ['PROJECT_ID']
        model_repo = os.environ['MODEL_REPO']

        client = storage.Client(project=project_id)
        bucket = client.get_bucket(model_repo)
        blob = bucket.blob('depl_model.pkl')
        blob.download_to_filename('/tmp/depl_model.pkl')
        # Load RandomForestRegressor model
        model = joblib.load('/tmp/depl_model.pkl')
        print(model, file=sys.stdout)
        sys.stdout.flush()
        print(json.dumps(prediction_input), file=sys.stdout)
        sys.stdout.flush()
        df = pd.read_json(json.dumps(prediction_input), orient='records')
        print(df, file=sys.stdout)
        sys.stdout.flush()
        y_pred = model.predict(df)
        print(y_pred, file=sys.stdout)
        sys.stdout.flush()
        print(y_pred[0], file=sys.stdout)
        sys.stdout.flush()
        # return the prediction outcome as a json message. 200 is HTTP status code 200, indicating successful completion
        return jsonify({'result': str(y_pred[0])}), 200
