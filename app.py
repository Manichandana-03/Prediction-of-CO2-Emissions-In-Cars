from flask import Flask,render_template,request
import pickle
import numpy as np

app=Flask(__name__)
model = pickle.load(open("modal.pkl","rb"))

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predict():
    enginesize=int(request.form.get('enginesize'))
    cylinders = int(request.form.get('cylinders'))
    fuelconsumptioncity=int(request.form.get('fuelconsumptioncity'))
    fuelConsumptionhwy=int(request.form.get('fuelConsumptionhwy'))
    fuelconsumptioncomb=int(request.form.get('fuelconsumptioncomb'))
    fuelconsumptioncombMpg=int(request.form.get('fuelconsumptioncombMpg'))
    array_a = [np.array([enginesize,cylinders,fuelconsumptioncity,fuelconsumptioncomb,fuelconsumptioncombMpg,fuelConsumptionhwy])]
    prediction = model.predict(array_a)
    return render_template('index.html',prediction="Predicted Value: {}".format(*prediction))

if __name__ == "__main__":
    app.run(debug=True)