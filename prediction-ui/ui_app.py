# importing Flask and other modules
import json

import requests
from flask import Flask, request, render_template

# Flask constructor
app = Flask(__name__)


# A decorator used to tell the application
# which URL is associated function
@app.route('/predictprice', methods=["GET", "POST"])
def predict_price():
    if request.method == "POST":
        prediction_input = [
            {
                "crim": int(request.form.get("crim")),  # getting input with name = crim in HTML form
                "nox": int(request.form.get("nox")),  # getting input with name = nox in HTML form
                "rm": int(request.form.get("rm")),
                "dis": int(request.form.get("dis")),
                "ptratio": int(request.form.get("ptratio")),
                "lstat": float(request.form.get("lstat"))
            }
        ]
        print(prediction_input)
        # use requests library to execute the prediction service API by sending a HTTP POST request
        # localhost or 127.0.0.1 is used when the applications are on the same machine.
        res = requests.post('http://localhost:5000/price_predictor/', json=json.loads(json.dumps(prediction_input)))
        print(res.status_code)
        result = res.json()
        return result
    return render_template(
        "user_form.html")  # this method is called of HTTP method is GET, e.g., when browsing the link


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
