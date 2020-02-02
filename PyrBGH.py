# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 20:36:56 2020

@author: brand
"""

import pyrebase
import json
import pandas as pd
from sklearn.externals import joblib
import numpy as np



config = {
  "XXXXXXXX"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
#db.child("users").order_by_child("name").limit_to_first(3).get()
dataGet = db.child("data/Calibrated/plastic").get()
df = pd.DataFrame.from_dict(dataGet.val())

df_t = df.T
df_t = df_t.drop('ts')


df_t1 =df_t['specs'].str.split(",",expand = True)
df_r = pd.concat([df_t1,df_t['Recyclable']],axis=1)
df_r['Recyclable'] = np.where(df_r['Recyclable'] == 'No',0,1)

df_t1 = df_t1.astype(float)

predr = df_t1.iloc[-1].values

predrs = predr.reshape(1,-1)

tlf = joblib.load('model.joblib')
preds = tlf.predict(predrs)
jsoner = predrs.tolist()
jsonSpec = json.dumps(jsoner)
data = {"user":101,"prediction" : str(preds)[1], "spectrum": str(jsonSpec)}
db.child("results").push(data)


