# importing Flask and other modules
import json
import os

import requests
from flask import Flask, request, render_template

# Flask constructor
app = Flask(__name__)

import os

# A decorator used to tell the application
# which URL is associated function
@app.route('/predictprice', methods=["GET", "POST"])
def predict_price():
    if request.method == "POST":
        prediction_input = [
            {
                "crim": float(request.form.get("crim")),  # getting input with name = crim in HTML form
                "nox": float(request.form.get("nox")),  # getting input with name = nox in HTML form
                "rm": int(request.form.get("rm")),
                "dis": float(request.form.get("dis")),
                "ptratio": float(request.form.get("ptratio")),
                "lstat": float(request.form.get("lstat"))
            }
        ]
        print(prediction_input)
        # use requests library to execute the prediction service API by sending a HTTP POST request
        # localhost or 127.0.0.1 is used when the applications are on the same machine.
        api_url = os.environ['PREDICTION_API_URL']
        api_port = os.environ['PREDICTION_API_PORT']
        request_url_with_port = "{0}:{1}/price_predictor".format(api_url,api_port)
        request_url = "{1}/price_predictor".format(api_url)
        res = requests.post(request_url, json=json.loads(json.dumps(prediction_input)))
        print(res.status_code)
        result = res.json()
        return result
    return render_template(
        "user_form.html")  # this method is called of HTTP method is GET, e.g., when browsing the link


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
