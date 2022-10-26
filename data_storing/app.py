from resources.data_storing import DataStoring
import logging
from flask import Flask, jsonify, Response, request

app=Flask(__name__)
app.config["DEBUG"] = True

logger = logging.getLogger('werkzeug') # grabs underlying WSGI logger
handler = logging.FileHandler('test.log') # creates handler for the log file
logger.addHandler(handler) # adds handler to the werkzeug WSGI logger

@app.route('/post_json', methods=['POST'])
def store_data():
    logger.info('test')
    if DataStoring.store_posted_data:
        return "Data stored succesfully"
    else:
        return "Content type not supported"

app.run(host='0.0.0.0', port=5002)
