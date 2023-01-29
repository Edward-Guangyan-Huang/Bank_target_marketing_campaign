import numpy as np
from flask import Flask, request,render_template
import pickle
from transitioner import Transitioner

app = Flask(__name__)
bank_marketing_model = pickle.load(open('bank_marketing_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    features = [x for x in request.form.values()]
    prediction = bank_marketing_model.predict([Transitioner(features)])

    output = int(prediction)

    if output == 0:
        return render_template('index.html', prediction_text='This client is not likely to purchase the product'.format(output))
    elif output == 1:
        return render_template('index.html', prediction_text='This client is likely to purchase the product'.format(output))

if __name__ == "__main__":
    app.run(debug=True)
