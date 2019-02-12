import os

# TensorFlow and tf.keras
import keras
from keras.models import load_model
from keras.utils import CustomObjectScope
from keras.initializers import glorot_uniform


# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

FEELINGS = ['angry', 'sad', 'happy', 'neutral']

with CustomObjectScope({'GlorotUniform': glorot_uniform()}):
    model = load_model('fonetic.h5')

    test_images = []
    test_labels = []
    for feeling in FEELINGS:
        for filename in os.listdir('test_data/' + feeling):
            path = 'test_data/' + feeling + '/' + filename
            image= Image.open(path)
            test_images.append(np.asarray(image))
            test_labels.append(FEELINGS.index(feeling))

    test_images = np.asarray(test_images)
    test_labels = np.asarray(test_labels)

    test_loss, test_acc = model.evaluate(test_images, test_labels)

    print('Test accuracy:', test_acc)