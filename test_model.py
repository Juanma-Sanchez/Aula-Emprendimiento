# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

FEELINGS = ['angry', 'sad', 'happy', 'neutral']

model = load_model('fonetic.h5')

#TODO read and generate testing dataset
test_images = []
test_labels = []

test_loss, test_acc = model.evaluate(test_images, test_labels)

print('Test accuracy:', test_acc)