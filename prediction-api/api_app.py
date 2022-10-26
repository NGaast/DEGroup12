from flask import Flask, request

from price_predictor import PricePredictor

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/price_predictor/', methods=['POST']) # path of the endpoint. Except only HTTP POST request
def predict_str():
    # the prediction input data in the message body as a JSON payload
    prediction_input = request.get_json()
    return dp.predict_single_record(prediction_input)


dp = PricePredictor()
app.run(host='0.0.0.0', port=5000)
