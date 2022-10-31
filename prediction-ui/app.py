# importing Flask and other modules
import json
import os
import sys
import secrets

import requests
from flask import Flask, request, render_template

# Flask constructor
app = Flask(__name__)

secret = secrets.token_urlsafe(32)
app.secret_key = secret

# A decorator used to tell the application
# which URL is associated function
@app.route('/predictprice', methods=["GET", "POST"])
def predict_price():
    if request.method == "POST":
        # Prepare json request
        prediction_input = [
            {
                "CRIM": float(request.form.get("crim")),
                "NOX": float(request.form.get("nox")),
                "RM": int(request.form.get("rm")),
                "DIS": float(request.form.get("dis")),
                "PTRATIO": float(request.form.get("ptratio")),
                "LSTAT": float(request.form.get("lstat"))
            }
        ]
        # Build API endpoint from environment variables
        api_url = os.environ['PREDICTION_API_URL']
        api_endpoint = os.environ['PREDICTION_API_ENDPOINT']
        predict_url = "{0}/{1}".format(api_url, api_endpoint)

        # Send POST request to prediction url
        res = requests.post(predict_url, json=json.loads(json.dumps(prediction_input)))
        return res.json()
    return render_template("user_form.html")  # this method is called of HTTP method is GET, e.g., when browsing the link

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
