from flask import Flask, jsonify, Response, request

app=Flask(__name__)
app.config["DEBUG"] = True

@app.route('/post_json', methods=['POST'])
def store_data():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        return json
    else:
        return 'Content-Type not supported!'

app.run(host='0.0.0.0', port=5000)
