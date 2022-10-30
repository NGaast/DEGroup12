from flask import Flask, jsonify, Response, request, render_template, flash, redirect

import requests
import sys
import os
import json
import secrets

app=Flask(__name__)

secret = secrets.token_urlsafe(32)
app.secret_key = secret


@app.route('/training_ui', methods=['GET', 'POST'])
def training_ui():
    if request.method == "POST":
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

        request_path = os.environ['TRAINING_API']
        upload_endpoint = os.environ['UPLOAD_ENDPOINT']
        train_endpoint = os.environ['TRAIN_ENDPOINT']
        upload_url = "{0}/{1}".format(request_path, upload_endpoint)
        train_url = "{0}/{1}".format(request_path, train_endpoint)
        upload_request = requests.post(upload_url, json=json.load(data_file))
        return upload_request.json()
    return render_template("training_template.html")  # this method is called of HTTP method is GET, e.g., when browsing the link
    
@app.route('/train_model', methods=['POST'])
def train_model():
    if request.method == "POST":
        request_path = os.environ['TRAINING_API']
        train_endpoint = os.environ['TRAIN_ENDPOINT']
        train_url = "{0}/{1}".format(request_path, train_endpoint)
        upload_request = requests.post(upload_url)
        return upload_request.json()

app.run(host='0.0.0.0', port=5000)
