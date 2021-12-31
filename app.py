from flask import Flask, request
import pandas as pd
import numpy as np
import pickle
from flasgger import Swagger


app = Flask(__name__)
Swagger(app)

input_ = open('randomForest.pkl', 'rb')
model = pickle.load(input_)




@app.route('/')
def test():
    return "hey"

@app.route('/predict')
def predict():

    """
    Enter Bank note details -
    ---
    parameters:
        - name: variance
          in: query
          type: number
          required: true
        - name: skewness
          in: query
          type: number
          required: true
        - name: curtosis
          in: query
          type: number
          required: true
        - name: entropy
          in: query
          type: number
          required: true

    responses:
        200:
            description: The output value is

    """

    var = request.args.get('variance')
    skew = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    pred = model.predict([[var, skew, curtosis, entropy]])
    return str(pred)


if __name__=='__main__':
    app.run(host='0.0.0.0')