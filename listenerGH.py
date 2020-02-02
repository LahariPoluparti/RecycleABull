# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 02:39:46 2020

@author: brand
"""
import pyrebase
import json
import pandas as pd
from sklearn.externals import joblib
import numpy as np



config = {
  "apiKey": "XXXXXXXXXXXXXXXXXXXX",
  "authDomain": "XXXXXXXXXXXXXXXX",
  "databaseURL": "XXXXXXXXXXXXXXX",
  "storageBucket": "XXXXXXXXXXXXX",
  "serviceAccount": "XXXXXXXXXXXX"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

def stream_handler(message):
    print(message["event"]) # put
    print(message["path"]) # /-K7yGTTEp7O549EzTYtI
    print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}
    
    if(message["event"] == "put"):
        if isinstance(message["data"], str):
            dfx = message["data"]
            classer(dfx)
            
def classer(dataf):
    newdat = dataf.split(',')
    dax = np.array(newdat, dtype=np.float32)
    daxrs = dax.reshape(1,-1)

    print(daxrs)
    tlf = joblib.load('model.joblib')
    
    predrs = tlf.predict(daxrs)
    jsoner = daxrs.tolist()
    jsonSpec = json.dumps(jsoner)
    data = {"user":101,"prediction" : str(predrs)[1], "spectrum": str(jsonSpec)}
    db.child("results").push(data)
    
    
my_stream = db.child("data/Calibrated/plastic").stream(stream_handler)

while True:
    data = input("[{}] Type exit to disconnect: ".format('?'))
    if data.strip().lower() == 'exit':
        print('Stop Stream Handler')
        if my_stream: my_stream.close()
        break