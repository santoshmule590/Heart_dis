from Model.utils import HeartAttack
from flask import Flask,jsonify,render_template,request
import config


app = Flask(__name__)

@app.route("/")
def hello_flask():
    print("We are in Flask API")
    return render_template("index.html")

@app.route("/Heart_disease",methods=['POST'])
def disease():
    age=int(request.form.get('age'))
    sex=int(request.form.get('sex'))
    cp=int(request.form.get('cp'))
    trestbps=int(request.form.get('trestbps'))
    chol=int(request.form.get('chol'))
    fbs=int(request.form.get('fbs'))
    restecg=int(request.form.get('restecg'))
    thalach=int(request.form.get('thalach'))
    exang=int(request.form.get('exang'))
    oldpeak=float(request.form.get('oldpeak'))
    slope=int(request.form.get('slope'))
    ca=int(request.form.get('ca'))
    thal=int(request.form.get('thal'))

    Obj = HeartAttack(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
    result= Obj.get_heart_classification()
    return render_template("index.html",prediction=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=config.PORT_NUMBER,debug=True)