# -*- coding: utf-8 -*-

Original file is located at
    https://colab.research.google.com/drive/1kFvaNyOH_0GHeBlnE5zG6BD2L0M-KTcM
"""

import tensorflow as tf
import numpy as np
import pandas as pd

data = pd.read_csv('/content/MASTERFILE.csv',header=None)

data.describe()

data.head()

data = data.astype('float32')

data.head()

data = data.to_numpy()

data.shape

training = data[:510]
testing = data[800:]

print(training.shape)
print(testing.shape)

training_features = training[:,0:-1]
training_labels = training[:,-1]
testing_features = training[:,0:-1]
testing_labels = training[:,-1]

print(training_features.shape)
print(training_labels.shape)

training_features[0].shape

print(training_features[0])

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Dense, Dropout, Activation

model = Sequential()
model.add(Input(shape=(362,)))
model.add(Dense(1,activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(362,activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(1,activation='sigmoid'))

model.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(training_features,training_labels,epochs=100,validation_data=(testing_features,testing_labels))

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import  Dense, Activation

model = Sequential([
    Dense(10, activation = "relu"),
    Dense(1, activation = "sigmoid")])

model.compile(
    optimizer = "rmscrop",
    loss = "binary_crossentropy")

model.fit(
    [[1, 2], [1, 3], [1, 1], [2, 2], [2, 3]],
    [True, False, False, True, True])

print(model.predict([[1, 2], [1, 3], [1, 1], [2, 2], [2, 3]]))
