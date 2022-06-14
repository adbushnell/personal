'''
Author : Albert Tran
Created: 2021-01-30

A script to kick off a small web-app for making predictions.
The model served will be a local model saved to disk.

'''

# %%
# ------------------------------------------------------------------------------
# Tracking URI
# ------------------------------------------------------------------------------
tracking_uri = r'file:///model_code/model'


# %%
# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------
import json
import mlflow
import pandas as pd
import waitress

from flask import Flask, request


# %%
# ------------------------------------------------------------------------------
# Retrieve the model
# ------------------------------------------------------------------------------
model = mlflow.sklearn.load_model(tracking_uri)


# %%
# ------------------------------------------------------------------------------
# App Definition
# ------------------------------------------------------------------------------
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    print('route: /')

@app.route('/echo', methods=['GET','POST'])
def echo():
    if request.method == 'GET':
        print('route: /echo (GET)')
    if request.method == 'POST':
        print('route: /echo (POST)')
    print(request.data)
    return request.data

@app.route('/invocations', methods=['POST'])
def predict():
    '''
    Assume data comes in as JSON in the list of dictionaries format.
    '''
    X_df  = pd.DataFrame(json.loads(request.data))
    y_hat = model.predict(X_df).tolist()
    response = json.dumps(y_hat)
    print(f'Prediction performed on {len(X_df)} samples.')
    return response



# Kick off the server
waitress.serve(app, host='0.0.0.0', port=1337)








