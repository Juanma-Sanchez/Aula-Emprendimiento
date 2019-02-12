import os
import wave

from PIL import Image

from audio_format import AudioFormatter

feelings = ['neutral', 'angry', 'sad', 'happy']

for feeling in feelings:
    audio_number = 0
    for filename in os.listdir('raw_audio/' + feeling):

        audio_number += 1

        path = 'raw_audio/' + feeling + '/' + filename
        audio = wave.open(path, 'rb')
        frames = [0]*72960
        for i in range(audio.getnframes()):
            frames[i] = int.from_bytes(audio.readframes(1), 'little')

        im = AudioFormatter.format(frames)
        image_name = filename.split('.')[0] + '.png'
        if audio_number <= 375:
            image_path = 'training_data/' + feeling + '/' + image_name
        else:
            image_path = 'test_data/' + feeling + '/' + image_name
        im.save(image_path, format='PNG')

