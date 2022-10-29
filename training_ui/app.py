from resources.model_training import ModelManaging
from flask import Flask, jsonify, Response, request, render_template, flash, redirect

import requests
import sys
import os

app=Flask(__name__)
app.config["DEBUG"] = True

@app.route('/training_ui', methods=['GET', 'POST'])
def training_ui():
    if request.method == 'POST':
        # No file in request
        if 'training_data' not in request.files:
            flash("No file in request")
            return redirect(request.url)
        # Retrieve file
        data_file = request.files['training_data']
        # No file
        if data_file.filename == '':
            flash("No file selected")
            return redirect(request.url)

        request_url
        res = requests.post(request_url, json=json.loads(json.dumps(prediction_input)))
    return render_template(
        "training_template.html")  # this method is called of HTTP method is GET, e.g., when browsing the link
    

app.run(host='0.0.0.0', port=5000)
