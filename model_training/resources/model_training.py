import argparse
import json

from symbol import parameters
from typing_extensions import Self
from google.cloud import storage, aip
from flask import Flask, jsonify, Response, request
import pandas as pd



class ModelManaging:
    def store_training_data():
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json_post = request.get_json()
            df = pd.DataFrame.from_dict(json_post)
            # Save to GCS as lr_model.pkl
            client = storage.Client(project="de-2022-ng")
            bucket = client.get_bucket("data_de2022_ng")
            blob = bucket.blob('dataset_test.csv')
            # Upload the locally saved model
            blob.upload_from_string(df.to_csv(), content_type='application/json')
            return True
        return False

    def run_pipeline_job(name, pipeline_def, pipeline_root, parameter_dict):
        # Opening JSON file
        f = open(  )
        data = json.load(f)
        job = aip.PipelineJob(
            display_name=name,
            enable_caching=False,
            template_path=pipeline_def,
            pipeline_root=pipeline_root,
            parameter_values=data)
        job.run()

    def parse_command_line_arguments():
            parser = argparse.ArgumentParser()
            parser.add_argument('--name', type=str, help="Pipeline Name")
            parser.add_argument('--pipeline_def', type=str, default="pipeline.json", help="Pipeline JSON definition file")
            parser.add_argument('--pipeline_root', type=str, help="GCP bucket for pipeline_root")
            parser.add_argument('--parameter_dict', type=str, help="Pipeline parameters as a json file")
            args = parser.parse_args()
            return vars(args)

    def train_model():
        Self.run_pipeline_job(**Self.parse_command_line_arguments)


        