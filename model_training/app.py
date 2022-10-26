from resources.model_training import ModelManaging
from flask import Flask, jsonify, Response, request

import sys
import os

app=Flask(__name__)
app.config["DEBUG"] = True

@app.route('/training_data', methods=['POST'])
def store_data():
    if ModelManaging.store_training_data():
        return "Data stored succesfully"
    else:
        return "Content type not supported"
    
@app.route('/train_model', methods=['POST'])
def train_model():
    pipeline_name = os.environ['PIPELINE_NAME']
    pipeline_template = os.environ['PIPELINE_TEMPLATE']
    pipeline_folder = os.environ['PIPELINE_FOLDER']
    pipeline_parameters = os.environ['PIPELINE_PARAMETERS']
    if ModelManaging.run_pipeline_job("housing-price",
                                      "./house_pricing_training_pipeline.json",
                                      "gs://de_jads_temp_ng",
                                      "./parameters.json"):
        return "Model trained succesfully"
    else:
        return "Model failed to train"
    

app.run(host='0.0.0.0', port=5000)
