from resources.data_storing import DataStoring
from flask import Flask, jsonify, Response, request

app=Flask(__name__)
app.config["DEBUG"] = True

@app.route('/post_json', methods=['POST'])
def store_data():
    if DataStoring.store_posted_data():
        return "Data stored succesfully"
    else:
        return "Content type not supported"

app.run(host='0.0.0.0', port=5002)
