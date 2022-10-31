from flask import Flask, jsonify, Response, request, render_template, flash, redirect

import requests
import sys
import os
import json
import secrets
import logging

app=Flask(__name__)

app.config['UPLOAD_FOLDER'] = "./tmp"

secret = secrets.token_urlsafe(32)
app.secret_key = secret


@app.route('/training_ui', methods=['GET', 'POST'])
def training_ui():
    return render_template("training_template.html")  # this method is called of HTTP method is GET, e.g., when browsing the link

@app.route('/upload_data', methods=['GET', 'POST'])
def upload_data():
    if request.method == "POST":
        # No file in request
        if 'training_data' not in request.files:
            print("No file in request", file=sys.stdout)
            sys.stdout.flush()
            return redirect(request.url)
        # Retrieve file
        data_file = request.files['training_data']
        # No file
        if data_file.filename == '':
            print("No file selected", file=sys.stdout)
            sys.stdout.flush()
            return redirect(request.url)

        request_path = os.environ['TRAINING_API']
        upload_endpoint = os.environ['UPLOAD_ENDPOINT']
        upload_url = "{0}/{1}".format(request_path, upload_endpoint)
        print(upload_url, file=sys.stdout)
        sys.stdout.flush()
        json_format = json.load(data_file)
        print(json_format, file=sys.stdout)
        sys.stdout.flush()
        upload_request = requests.post(upload_url, json=json_format)
        # Flush stdout to print in console
        return redirect('/training_ui')
    return redirect('/training_ui')
    
@app.route('/train_model', methods=['POST'])
def train_model():
    if request.method == "POST":
        flash('Running pipeline')
        request_path = os.environ['TRAINING_API']
        train_endpoint = os.environ['TRAIN_ENDPOINT']
        train_url = "{0}/{1}".format(request_path, train_endpoint)
        train_request = requests.post(train_url)
        return train_request.json()
    return redirect('/training_ui')

app.run(host='0.0.0.0', port=5000)
