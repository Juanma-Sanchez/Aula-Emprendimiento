import json
import os

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

FEELINGS = ['angry', 'sad', 'happy', 'neutral']


train_images_list = []
train_labels = []
for feeling in FEELINGS:
    for filename in os.listdir('training_data/' + feeling):
        path = 'training_data/' + feeling + '/' + filename
        image= Image.open(path)
        train_images_list.append(np.asarray(image))
        train_labels.append(FEELINGS.index(feeling))

train_images = np.asarray(train_images_list)
train_labels = np.asarray(train_labels)

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(65, 570)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(4, activation=tf.nn.softmax)
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=25)

model.save('fonetic.h5')

# save as JSON
json_string = model.to_json()
with open('fonetic.json', 'w') as outfile:
    json.dump(json_string, outfile)
