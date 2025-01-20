from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

model_file = open('rumah.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', unique_viwers=0)
@app.route('/predict', methods=['POST'])
def predict():
    LT = float(request.form['LT'])
    LB = float(request.form['LB'])
    JKT = float(request.form['JKT'])
    JKM = float(request.form['JKM'])
    GRS = float(request.form['GRS'])
    
    x=np.array([[LT,LB,JKT,JKM,GRS]])
    
    
    prediction = model.predict(x)
    output = round(prediction[0])
    hasil=(f"Rp.{output:,}")

    #return render_template('index.html', insurance_cost=output, age=age, sex=sex, smoker=smoker)
    return render_template('index.html', unique_viwers=hasil)

if __name__ == '__main__':
    app.run(debug=True)