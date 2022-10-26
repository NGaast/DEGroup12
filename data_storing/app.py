from resources.Data_storing import Database
from flask import Flask, jsonify, Response


app=Flask(__name__)
db = Database()

@app.route('/store-data', methods=['POST'])
def store_data():
    db.store_tables()
    return jsonify({'message' : 'Data stored successfully!'}), 200

@app.route('/read-data/<table_name>', methods=['GET'])
def read_data(table_name):
    return Response(db.read_table(table_name).to_json(orient='records'), status=200, mimetype='application/json')

with app.app_context():
    store_data()

app.run(host='0.0.0.0', port=5000)
