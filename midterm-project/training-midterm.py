
from types import DynamicClassAttribute
import pandas as pd
import numpy as np

df = pd.read_csv('heart_failure.csv')


 

# so the above model can be used to predict the probbility of someone dying of a heart attack


# so we have established here that the field sex has a binary attribute 
#this should indicate as either male or female
# so next is to convert it

#also the death event field is also
# indicating it is aslo a binary attribute 


#An ejection fraction (EF) is the volumetric fraction (or portion of the total) of fluid (usually blood) 
#ejected from a chamber (usually the heart) with each contraction (or heartbeat). 
#It can refer to the cardiac atrium, ventricle, gall bladder, or leg veins,
# although if unspecified it usually refers to the left ventricle of the heart. 
#EF is widely used as a measure of the pumping efficiency of the heart and is used to classify heart failure types. 
#It is also used as an indicator of the severity of heart failure, although it has recognized limitations.

survival_rate={
    1:'high',
    0:'low'
}


df.DEATH_EVENT=df.DEATH_EVENT.map(survival_rate)

gender={
    1:'male',
    0:'female'
    
}

df.sex=df.sex.map(gender)

anaemic={
    0:'non_amaemic',
    1:'anaemic'
}

df.anaemia=df.anaemia.map(anaemic)

smoker={
    0:'non_smoker',
    1:'smoker'
}

df.smoking=df.smoking.map(smoker)


diabetic={
    0:'non_diabetic',
    1:'diabetic'
}
df.diabetes =df.diabetes.map(diabetic)
blood_pressure={
    0:'normal_bp',
    1:'high_bp'
}

df.high_blood_pressure=df.high_blood_pressure.map(blood_pressure)

from sklearn.model_selection import train_test_split
df_full_train , df_test = train_test_split(df, test_size=0.2,random_state=1)
df_train,df_val = train_test_split(df_full_train , test_size=0.25,random_state=1)

len(df_train),len(df_test),len(df_val)

df_train=df_train.reset_index(drop=True)
df_test=df_test.reset_index(drop=True)
df_val=df_val.reset_index(drop=True)

y_train=(df_train.DEATH_EVENT=='high')
y_test=(df_test.DEATH_EVENT=='high')
y_val=(df_val.DEATH_EVENT=='high')

from sklearn.model_selection import KFold
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

numerical= ['age','creatinine_phosphokinase','ejection_fraction','serum_creatinine','serum_sodium','time']
categorical=['anaemia','diabetes','high_blood_pressure','sex','smoking']
def predict(df,dv,model):
    dicts = df[categorical+numerical].to_dict(orient='records')
    x=dv.transform(dicts)
    y_pred=model.predict_proba(x)[:,1]
    
    return y_pred

df_train.DEATH_EVENT.values

def train(df_train,y_train,C=1.0):
    dicts=df_train[categorical+numerical].to_dict(orient='records')
    
    dv= DictVectorizer(sparse=False)
    x_train=dv.fit_transform(dicts)
    
    model=LogisticRegression(C=C, max_iter=1000)
    model.fit(x_train,y_train)
    
    return dv,model

C=1.0
n_splits=5

kfold=KFold(n_splits,shuffle=True,random_state=1)
scores=[]
fold=0
for train_idx,val_idx in kfold.split(df_full_train):
    df_train=df_full_train.iloc[train_idx]
    df_val=df_full_train.iloc[val_idx]
    df_train.DEATH_EVENT=(df_train.DEATH_EVENT=='high').astype(int)
    df_val.DEATH_EVENT=(df_val.DEATH_EVENT=='high').astype(int)
    y_train=df_train.DEATH_EVENT.values
    y_val=df_val.DEATH_EVENT.values
    
    
    dv,model=train(df_train,y_train,C=C)
    y_pred=predict(df_val,dv,model)
    
    auc =roc_auc_score(y_val,y_pred)
    scores.append(auc)
    
    print(f'auc on fold{fold} is {auc}')
    
    fold=fold+1

print('validation results:')
print(' for C=%s the mean value is %.3f and the standard deviation is -/+ %.3f' %(C,np.mean(scores),np.std(scores)))

import pickle

output_file=f'model_C={C}.bin'
output_file

with open(output_file,'wb') as f_out:
    pickle.dump((dv,model),f_out)
    
print(f'the model is saved to{output_file}')

#using decision trees
