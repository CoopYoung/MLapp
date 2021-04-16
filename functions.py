from sklearn import datasets
from joblib import load
import numpy as np
import json

#load the model

my_model = load('log_model.pkl')




def my_prediction(data):

  dummy = np.array(data)
  dummyT = dummy.reshape(1,-1)
  r = dummy.shape
  t = dummyT.shape
  r_str = json.dumps(r)
  t_str = json.dumps(t)
  predictions = my_model.predict(dummyT) 
 #score = logisticRegr.score(x_test, y_test) #Computes final "accuracy score"
#print(score)
  #name = death[predictions]
  #name = name.tolist()
  #name_str = json.dumps(str(predictions[0]))
  #string = [t_str, r_str, name_str]
  return str(predictions[0])
