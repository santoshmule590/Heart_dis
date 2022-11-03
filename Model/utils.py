import numpy as np
import pandas as pd
import json
import pickle

import config


class HeartAttack():
    def __init__(self,age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):
        self.age = age
        self.sex = sex
        self.cp = cp
        self.trestbps =trestbps
        self.chol = chol
        self.fbs = fbs
        self.restecg = restecg
        self.thalach = thalach
        self.exang = exang
        self.oldpeak = oldpeak
        self.slope = slope
        self.ca = ca
        self.thal = thal

    def load_model(self):
         with open (config.JSON_FILE_PATH,"r") as f:
             self.json_dict = json.load(f)
         with open (config.MODEL_FILE_PATH,"rb") as f:
             self.model = pickle.load(f)



        # with open (r"C:\Users\ADMIN\Desktop\Classification Algorithm\37_Santosh_Mule_Logistic_heart_dataset\Model\Heart.json","r") as f:
        #     self.json_dict=json.load(f)
        
        # with open (r"C:\Users\ADMIN\Desktop\Classification Algorithm\37_Santosh_Mule_Logistic_heart_dataset\Model\Heart.pkl","rb") as f:
        #     self.model=pickle.load(f)

    def get_heart_classification(self):
        self.load_model()
        array = np.zeros(len(self.json_dict["column"]))

        array[0]=self.age
        array[1]=self.sex
        array[2]=self.cp
        array[3]=self.trestbps
        array[4]=self.chol
        array[5]=self.fbs
        array[6]=self.restecg
        array[7]=self.thalach
        array[8]=self.exang
        array[9]=self.oldpeak
        array[10]=self.slope
        array[11]=self.ca
        array[12]=self.thal

        print("Array is ::\n",array)


        result = self.model.predict([array])[0]

        result1 = "You have symptoms of Heart Attack" if result == 1 else "You are Healthy !!!"

        return result1

if __name__ == "__main__":
    age = 50.0
    sex = 0
    cp =0
    trestbps= 130.0
    chol = 285.0
    fbs= 1
    restecg= 1.0
    thalach= 180.0
    exang = 1.0
    oldpeak = 0.2
    slope = 1.0
    ca = 0.0
    thal = 2.0
   
    Obj = HeartAttack(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
    result= Obj.get_heart_classification()
    print(result)



