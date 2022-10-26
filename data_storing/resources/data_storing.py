import os
from google.cloud import storage
import sys
from flask import Flask, jsonify, Response, request
import pandas as pd
import json


class DataStoring:
    def store_posted_data():
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json_post = request.get_json()
            df = pd.read_json(json_post)
            # Save to GCS as lr_model.pkl
            client = storage.Client(project="de-2022-ng")
            bucket = client.get_bucket("model_repo_de2022_ng")
            blob = bucket.blob('dataset_test.csv')
            # Upload the locally saved model
            blob.upload_from_string(df.to_csv(), content_type='application/json')
            

            return True
        return False