import os
import requests
import pandas as pd
import sqlalchemy as db
from sqlalchemy import Float
from sklearn.model_selection import train_test_split

class Database:

    def __init__(self):
        db_url = os.environ['DB_URL'] if 'DB_URL' in os.environ else 'sqlite:///data.db'
        self.engine = db.create_engine(db_url)

    def create_table(self, d):
        d['data'].to_sql(d['table_name'], self.engine, if_exists='replace', index=False, dtype=Float)

    def read_table(self, table_name):
        return pd.read_sql_table(table_name, con=self.engine)

    def store_tables(self):
        [self.create_table(d) for d in self.get_data()]

    def get_data(self):
        try:
            data = requests.get(os.environ['DATAINGESTION_API']).json()
        except:
            data = requests.get(os.environ['DATAINGESTION_API']).json()
        X = pd.read_json(data['X'])
        y = pd.read_json(data['y'])
        dataframes = self.split_data(X, y)
        names = ['X_train', 'X_test', 'y_train', 'y_test']
        return [{'table_name':names[i], 'data': dataframes[i]} for i in range(4)]

    def split_data(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=0)
        dataFrames = []
        dataFrames.append(X_train)
        dataFrames.append(X_test)
        dataFrames.append(y_train)
        dataFrames.append(y_test)
        return dataFrames
