from resources.model_training import ModelManaging
from flask import Flask, jsonify, Response, request

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
    if ModelManaging.run_pipeline_job(**ModelManaging.parse_command_line_arguments):
        return "Model trained succesfully"
    else:
        return "Model failed to train"
    

app.run(host='0.0.0.0', port=5002)
