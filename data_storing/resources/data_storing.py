import os
from google.cloud import storage
from flask import Flask, jsonify, Response, request
import pandas as pd
import json



class DataStoring:
    def store_posted_data():
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json_post = request.json
            data = json.load(json_post)
            df = pd.read_json(data)
            # Save to GCS as lr_model.pkl
            client = storage.Client(project="de-2022-ng")
            bucket = client.get_bucket("model_repo_de2022_ng")
            blob = bucket.blob('dataset_test.csv')
            # Upload the locally saved model
            blob.upload_from_string(df.to_csv(), content_type='application/json')
           
            return True
        return False
