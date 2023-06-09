# -*- coding: utf-8 -*-
"""Diabetes_Original.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pI1SaT-7jJTgYUw6fkzXc1HSL3M9E9Jk
"""

import random
import numpy as np
import tensorflow as tf

random.seed(1693)
np.random.seed(1693)
tf.random.set_seed(1693)

from tensorflow import keras
import pandas as pd
from keras.models import Sequential
from keras.layers.core import Dense
from keras.utils import to_categorical
import matplotlib.pyplot as pyplot
import datetime as dt
from datetime import datetime
import sklearn as sk
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

df = pd.read_csv('diabetes_binary_health_indicators_BRFSS2015.csv')

df

fa = pd.get_dummies(df['GenHlth'])
new_cols_list = ['GenHealth1', 'GenHealth2', 'GenHealth3', 'GenHealth4', 'GenHealth5']
fa.columns = new_cols_list
df = df.drop(columns = ['GenHlth'])
df = df.join(fa)

fa = pd.get_dummies(df['Age'])
new_cols_list = ['Age1', 'Age2', 'Age3', 'Age4', 'Age5', 'Age6', 'Age7', 'Age8', 'Age9', 'Age10', 'Age11', 'Age12', 'Age13']
fa.columns = new_cols_list
df = df.drop(columns = 'Age')
df = df.join(fa)

fa = pd.get_dummies(df['Education'])
new_cols_list = ['Edu1', 'Edu2', "Edu3", 'Edu4', 'Edu5', 'Edu6' ]
fa.columns = new_cols_list
df = df.drop(columns = ['Education'])
df = df.join(fa)

fa = pd.get_dummies(df['Income'])
new_cols_list = ['Income1', 'Income2', "Income3", 'Income4', 'Income5', 'Income6', 'Income7', 'Income8' ]
fa.columns = new_cols_list
df = df.drop(columns = ['Income'])
df = df.join(fa)

df

cols = [x for x in df.columns if x != 'Diabetes_binary' ]
x = df[cols]
y = df[['Diabetes_binary']]

x_train, x_test, y_train, y_test = train_test_split(x, 
                                                    y, 
                                                    test_size=0.2, 
                                                    random_state=1693)

model = Sequential()
model.add(Dense(units = 16, input_dim = x_train.shape[1], activation = 'relu'))
model.add(Dense(units = 8, activation = 'relu'))
model.add(Dense(1, activation = 'sigmoid'))
model.summary()

model.compile(loss = 'BinaryCrossentropy', optimizer = 'adam', metrics = ['accuracy'])
estimate = model.fit(x_train, y_train, epochs = 5, validation_data = (x_test, y_test))

model.summary()

loss, accuracy = model.evaluate(x_test, y_test)
print('Test accuracy:', accuracy)

preds = model.predict(x_test)
predictions = [1 if x > 0.5 else 0 for x in preds]
actuals = [x for x in y_test['Diabetes_binary']]
confusion_matrix(actuals, predictions)

FN_rate = 6054/(6054+785+42917+980)
acc = (42917+980)/(42917+785+6054+980)
print(f"Our false negative rate (type ii error) is {FN_rate}")
print(f"Our accuracy rate is {acc}")