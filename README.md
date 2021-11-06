# miterm-project

for this project i was assessing how likely someone is going to get a heart attack

the data set is part of the resprotory

first you'd need to train the model  which is located in the train-midterm.py  file

 and then run the flask app which is located in the predict-midterm.py file
 
 
i added a bit more detail where the user of the model can in put a patient's name and the use can asssess the likely hood of the pateint getting a heart attack

this is can be done by runnin the command python predict-train.py

upon which the user will be prompted to enter the patient's key vitals

the model then zips the user inputs with their appropriate headers and then turn them into a json file which is the fed into the predict-midterm.py


after which an appropriate response will be given.



finally the model gives the name and the likelyhood of getting a heart attack and gives a warning on severe it can get


