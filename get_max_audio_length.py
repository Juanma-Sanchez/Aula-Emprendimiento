import wave

import os

feelings = ['neutral', 'angry', 'sad', 'happy']

max_length = 0
frame_rate = 0

for feeling in feelings:
    for filename in os.listdir('raw_audio/' + feeling):

        path = 'raw_audio/' + feeling + '/' + filename
        audio = wave.open(path, 'rb')
        n = audio.getnframes()
        if n > max_length:
            max_length = n
            frame_rate = audio.getframerate()

print(max_length, 'frames')
print('Frequency', frame_rate, 'Hz')