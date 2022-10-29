from resources.model_training import ModelManaging
from flask import Flask, jsonify, Response, request, render_template
import pandas as pd

import sys
import os

app=Flask(__name__)
app.config["DEBUG"] = True

@app.route('/train_model', methods=['GET', 'POST'])
def training_ui():
    if request.method == 'POST':
        data_file = request.files['training_data']
        

    return render_template(
        "template/training_template.html")  # this method is called of HTTP method is GET, e.g., when browsing the link
    

app.run(host='0.0.0.0', port=5000)
