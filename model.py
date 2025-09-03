from flask import Flask, request, jsonify, render_template
import pandas as pd
import pickle

app = Flask(__name__)

def get_cleaned_data(form):
    gestation = float(form['gestation'])
    parity = int(form['parity'])
    age = float(form['age'])
    height = float(form['height'])
    weight = float(form['weight'])
    smoke = float(form['smoke'])
      
    cleaned_data = {
        "gestation": [gestation],
        "parity": [parity],
        "age": [age],
        "height": [height],
        "weight": [weight],
        "smoke": [smoke]
    }
    return cleaned_data

@app.route('/', methods=['GET'])
def home():
    return render_template('model.html')   # simple HTML form

@app.route('/predict', methods=['POST'])
def get_prediction():
    # use request.form if data comes from an HTML form
    baby_data = request.form  

    baby_cleaned_data = get_cleaned_data(baby_data)
    data_df = pd.DataFrame(baby_cleaned_data)

    with open('model/model.pkl','rb') as obj:
        model = pickle.load(obj)

    prediction = model.predict(data_df)
    prediction = round(float(prediction), 2)

    # return prediction in HTML page
    return render_template('model.html', prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
