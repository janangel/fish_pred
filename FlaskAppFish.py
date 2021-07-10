
import numpy as np
import pickle
import pandas as pd
from flask import Flask, request
from flask import Flask, request, jsonify, render_template

app=Flask(__name__)
pickle_in = open("yy.pkl","rb")
classifier=pickle.load(pickle_in)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = classifier.predict(final_features)
    result = {0: 'Bream',  1: 'Parkki',  2: 'Perch',  3: 'Pike',  4: 'Roach',  5: 'Smelt', 6: 'Whitefish'}
    return render_template('index.html', prediction_text='The flower belong to species {}'.format(result[prediction[0]]))
    
    


if __name__=='__main__':
    app.run()