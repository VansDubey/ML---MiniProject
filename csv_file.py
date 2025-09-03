from flask import Flask, render_template,request

app = Flask(__name__)

# End Points:

@app.route('/',methods = ['GET'])
def home():
    return render_template('forms_csv.html')

@app.route('/upload',methods = ['POST'])
def get_data():
    file = request.files['file']
    print("This is what it contains:",file)
    print("file :", file)
    
    
    if file.filename.endswith('.csv'):
        path = 'userfile/' + file.filename
        file.save(path)
        return "We have received Your File"
    else:
        return "Upload a csv file only"    


if __name__  == '__main__':
    app.run(debug = True) 

