
import requests
import json

url = 'http://127.0.0.1:9696/predict-midterm'
casualty_vital=[]

print("dear medical personal please enter the data below:")
patients_name=input("please enter the patient's name  >  ")

age = int(input("how old is the patient  >  "))
anaemia= input("is the patient anaemic... choose between anaemic and non_anaemic  >   ")

creatinine_phosphokinase =int(input("please key in the patients creatinine phosphokinase  >  "))
diabetes=input("is the patient diabetic ... choose between diabetic and non_diabetic  >  ")

ejection_fraction=int(input("please enter the patients ejection fraction  >  "))

high_blood_pressure = input("does the patient suffer from high blood pressure.... please choose between high_bp and normal_bp  >  ")

platelets=int(input("please key in the platelet count  >  "))
serum_creatinine = float(input("please key in the serum creatinine level  >  "))

serum_sodium= int(input("please key in the serum sodium level  >  "))

sex=input("please indicate weather the patient is male or female  >  ")
time= int(input("please indicate the time  >  "))

smoking= input("please indicate whether the patient is a smoker or a non_smoker  >  ")
#casualty_vital.append(patients_name)
casualty_vital.append(age)
casualty_vital.append(anaemia)
casualty_vital.append(creatinine_phosphokinase)
casualty_vital.append(diabetes)
casualty_vital.append(ejection_fraction)
casualty_vital.append(high_blood_pressure)
casualty_vital.append(platelets)
casualty_vital.append(serum_creatinine)
casualty_vital.append(serum_sodium)
casualty_vital.append(sex)
casualty_vital.append(smoking)
casualty_vital.append(time)


b=[ 'age', 'anaemia', 'creatinine_phosphokinase', 'diabetes',
       'ejection_fraction', 'high_blood_pressure', 'platelets',
       'serum_creatinine', 'serum_sodium', 'sex', 'smoking', 'time' ]
print("fot the patient %s" %patients_name )
print("thier vitals are?")
print(casualty_vital) 

pateint_credential=dict(zip(b,casualty_vital))
print(pateint_credential)
#json_name=json.dumps(patients_name)
#json_casualty=json.dumps(casualty_vital)
pateint_json=json.dumps(pateint_credential)
print(pateint_json)
response =requests.post(url,json=pateint_json).json()
print(response) 
if response['DEATH_EVENT']==True:
    print(' book the patient for admission and and tag the pataint as a high alert individual %s'% patients_name)
    
else:
    print(' send the patient to the next doctor in line %s' % patients_name)
