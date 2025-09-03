## Jinga Template =>  {{ Placeholder for varaibles}}

## import the falsk app
from flask import Flask,jsonify,render_template   # Library and class

## create an instance

app = Flask(__name__)

## define the function  and route
#@app.route('/', methods =['GET'])
#def home():
#    return render_template('index.html', name= 'Vanshika')   # Used to render the HTML page

@app.route('/user')
def data():
    data = {'Name':'Vanshika',
            'Age':20}
    return jsonify(data)

@app.route('/about-us')
def aboutUs():
    return " <h1>About-us</h1>"

@app.route('/', methods =[
    'GET'])
def form():
    return render_template('forms.html')

@app.route('/form',methods = ['POST'])
def func():
    return "The form is submitted successfully"

## trigger the flask app
if __name__  == '__main__':
    app.run(debug = True)  # NOw you need to close and open teh application again , the changes will appear real time on your application