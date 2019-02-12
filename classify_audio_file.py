import sys
import wave
import math

# TensorFlow and tf.keras
import keras
from keras.models import load_model
from keras.utils import CustomObjectScope
from keras.initializers import glorot_uniform


# Helper libraries
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from scipy.signal import resample

from audio_format import AudioFormatter

FEELINGS = ['angry', 'sad', 'happy', 'neutral']

file_path = sys.argv[1]
audio_wave = wave.open(file_path, 'rb')
audio = np.asarray([int.from_bytes(audio_wave.readframes(1), 'little') for i in range(audio_wave.getnframes())])
number_of_samples = int(24414*audio_wave.getnframes()/audio_wave.getframerate())
resampled_audio = resample(audio, number_of_samples)
number_of_blocks = math.ceil(number_of_samples / 72960)
image_list = []

for block_number in range(number_of_blocks):
    frames = [0]*72960
    for i in range(72960):
        frames[i] = resampled_audio[72960*block_number:72960 + i]

    image = AudioFormatter.format(frames)
    image_list.append(np.asarray(image))

image_list = np.asarray(image_list)
result = [0]*4

with CustomObjectScope({'GlorotUniform': glorot_uniform()}):
    model = load_model('fonetic.h5')

    predictions = model.predict(image_list)
    for prediction in predictions:
        for i in range(len(FEELINGS)):
            result[i] += prediction[i]

    result = result * 100/number_of_blocks


    for i in range(4):
        print('Porcentaje de', FEELINGS[i], result[0])



