import json

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from flask import jsonify


class PricePredictor:
    def __init__(self):
        self.model = None

    def predict_single_record(self, prediction_input):
        print(prediction_input)
        df = pd.read_csv('DEGroup12/data/HousingData.csv')
        df = df.dropna()
        X = df.drop(['MEDV'], axis=1)
        y = df['MEDV']
        X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.9)
        model = RandomForestRegressor(random_state=0)
        model.fit(X_train, y_train)
        print(json.dumps(prediction_input))
        df = pd.read_json(json.dumps(prediction_input), orient='records')
        print(df)
        y_pred = model.predict(df)
        print(y_pred[0])
        status = (y_pred[0] > 0.5)
        print(type(status[0]))
        # return the prediction outcome as a json message. 200 is HTTP status code 200, indicating successful completion
        return jsonify({'result': str(status[0])}), 200
