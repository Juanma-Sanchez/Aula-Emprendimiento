# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

FEELINGS = ['angry', 'sad', 'happy', 'neutral']

# TODO load images and generate training dataset
train_images = []
train_labels = []

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(570, 65)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(4, activation=tf.nn.softmax)
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5)

model.save('fonetic.h5')
