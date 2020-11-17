#Creating Flask App
from flask import Flask, request
from flasgger import Swagger
import pandas as pd
import numpy as np
import pickle

app=Flask(__name__)
Swagger(app)
pickle_in=open('classifier.pkl','rb')
classifier=pickle.load(pickle_in)

@app.route('/')
def home():
    return 'Welcome'

           
@app.route('/predict',methods=['Get'])

def predict_note_authentication():
    """Let's Authenticate the Bonk Note
    This is using doc strings for specifications.
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
        description: The output values
  
    
    """
    variance=request.args.get('variance')
    skewness=request.args.get('skewness')
    curtosis=request.args.get('curtosis')
    entropy=request.args.get('entropy')
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    return 'The predicted  value is'+str(prediction)


@app.route('/predict_file', methods=["POST"])
def predict_note_file():
    """Let's Authenticate the Bonk Note
    This is using doc strings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
    responses:
        200:
            description: The output values
    """
    
    df_test=pd.read_csv(request.files.get("file"))
    prediction=classifier.predict(df_test)
    return 'The predicted values for csv '+str(list(prediction))

if __name__=='__main__':
    app.run()