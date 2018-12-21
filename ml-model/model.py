# -*- coding: utf-8 -*-
"""bng.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PuSTNTGm-KBCTXQXIWosmYObaAXvhxCg
"""

from google.colab import files
uploaded = files.upload()

import pandas as pd
import lightgbm as lgb
import numpy as np
import sklearn
import json
from pprint import pprint
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

train_X = pd.read_csv('train.csv')
train_Y = train_X['CLAIM_FLAG']
train_X = train_X.drop(['CLAIM_FLAG'],axis=1)

valid_X = pd.read_csv('valid.csv')
valid_Y = valid_X['CLAIM_FLAG']
valid_X = valid_X.drop(['CLAIM_FLAG'],axis=1)

test_X = pd.read_csv('test.csv')
test_Y = test_X['CLAIM_FLAG']
test_X = test_X.drop(['CLAIM_FLAG'],axis=1)

scaler = StandardScaler()
scaler.fit(train_X)

train_X = scaler.transform(train_X)
valid_X = scaler.transform(valid_X)
test_X = scaler.transform(test_X)

results = []

model = MLPClassifier(hidden_layer_sizes = (512,128,32), activation = 'logistic', learning_rate_init = 0.001, alpha = 0.03, max_iter = 5000)

#train the model
bst = model.fit(train_X,train_Y)

#get predictions
Y_pred = model.predict(valid_X)
Y_pred[np.where(Y_pred < 0.5)] = 0
Y_pred[np.where(Y_pred >= 0.5)] = 1

#calulate accuracy
acc = sklearn.metrics.accuracy_score(np.array(Y_pred), np.array(valid_Y))
f = sklearn.metrics.f1_score(np.array(valid_Y),np.array(Y_pred))  
print('valid_acc: ',acc)
print('f-score:', f)
