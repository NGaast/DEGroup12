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
        prediction_input = [
            {
                "CRIM": float(request.form.get("crim")),  # getting input with name = crim in HTML form
                "NOX": float(request.form.get("nox")),  # getting input with name = nox in HTML form
                "RM": int(request.form.get("rm")),
                "DIS": float(request.form.get("dis")),
                "PTRATIO": float(request.form.get("ptratio")),
                "LSTAT": float(request.form.get("lstat"))
            }
        ]
        # use requests library to execute the prediction service API by sending a HTTP POST request
        # localhost or 127.0.0.1 is used when the applications are on the same machine.
        api_url = os.environ['PREDICTION_API_URL']
        api_endpoint = os.environ['PREDICTION_API_ENDPOINT']
        predict_url = "{0}/{1}".format(api_url, api_endpoint)
        res = requests.post(predict_url, json=json.loads(json.dumps(prediction_input)))
    return render_template("user_form.html")  # this method is called of HTTP method is GET, e.g., when browsing the link

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
