
import pickle

from flask import Flask

from flask import request
from flask import jsonify
model_file = 'model_C=1.0.bin'

with open(model_file,'rb') as f_in:
    dv,model=pickle.load(f_in)
    
app = Flask('DEATH_EVENT')
@app.route('/predict-midterm',methods = ['POST'])

def predict():
    pateint_json=request.get_json()
    x=dv.tranform([pateint_json])
    y_pred=model.predict_proba(x)[0,1]
    DEATH_EVENT=y_pred>=0.65
    result={
        'DEATH_EVENT_Probality':float(y_pred),
        'DEATH_EVENT':bool(DEATH_EVENT)
    }
    
    return jsonify(result)


if __name__== "__main__":
    app.run(debug='0.0.0.0',port=9696)
    


