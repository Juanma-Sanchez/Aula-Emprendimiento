import sys
import wave
import math

# TensorFlow and tf.keras
import keras
from keras.models import load_model
from keras.utils import CustomObjectScope
from keras.initializers import glorot_uniform


# Helper libraries
from PIL import Image
import numpy as np

from audio_format import AudioFormatter

FEELINGS = ['angry', 'sad', 'happy', 'neutral']

file_path = sys.argv[1]
audio_wave = wave.open(file_path, 'rb')
audio = np.asarray([int.from_bytes(audio_wave.readframes(1), 'little') for i in range(audio_wave.getnframes())])
number_of_samples = audio_wave.getnframes()
number_of_blocks = math.ceil(number_of_samples/72960)
image_list = []

for block_number in range(number_of_blocks):
    if block_number != number_of_blocks - 1:
        block = audio[72960*block_number:72960*block_number + 72959].tolist()
    else:
        block = audio[72960*block_number:-1].tolist()
        block.extend([0]*(72960 - len(block)))

    image = AudioFormatter.format(block)
    image_list.append(np.asarray(image))

image_list = np.asarray(image_list)
result = [0]*4

with CustomObjectScope({'GlorotUniform': glorot_uniform()}):
    model = load_model('fonetic.h5')

    predictions = model.predict(image_list)
    for prediction in predictions:
        for i in range(len(FEELINGS)):
            result[i] += prediction[i]

    result = (100/number_of_blocks) * result

    for i in range(4):
        print('Percentage of', FEELINGS[i], result[0], '%')



