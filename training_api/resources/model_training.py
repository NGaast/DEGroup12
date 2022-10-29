import argparse
import json

from flask import Flask, request, render_template

from typing_extensions import Self
from google.cloud import storage
import google.cloud.aiplatform as aip
import pandas as pd



class ModelManaging:
    def store_training_data():
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json_post = request.get_json()
            df = pd.DataFrame.from_dict(json_post)
            # Drop NaN values
            df = df.dropna()
            # Save to GCS as lr_model.pkl
            client = storage.Client(project="de-2022-ng")
            bucket = client.get_bucket("data_de2022_ng")
            blob = bucket.blob('dataset.csv')
            # Upload the locally saved model
            blob.upload_from_string(df.to_csv(), content_type='application/json')
            return True
        return False

    def run_pipeline_job(name, pipeline_def, pipeline_root, parameter_dict):
        # Opening JSON file
        f = open(parameter_dict)
        data = json.load(f)
        job = aip.PipelineJob(
            display_name=name,
            enable_caching=False,
            template_path=pipeline_def,
            pipeline_root=pipeline_root,
            parameter_values=data)
        job.run()