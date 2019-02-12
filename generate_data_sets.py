import os, wave

from numpy.fft import fft, ifft
from numpy import array
from PIL import Image
import matplotlib.pyplot as plt


feelings = ['neutral', 'angry', 'sad', 'happy']
last_audio = []
# for feeling in feelings:
#     for filename in os.listdir('raw_audio/' + feeling):
#
#         path = 'raw_audio/' + feeling + '/' + filename
#         audio = wave.open(path, 'rb')
#         frames = [0]*72960
#         for i in range(audio.getnframes()):
#             frames[i] = int.from_bytes(audio.readframes(1), 'little')
#
#         last_audio = frames

path = 'raw_audio/sad/YAF_jar_sad.wav'
audio = wave.open(path, 'rb')
frames = [0]*72960
for i in range(audio.getnframes()):
    frames[i] = int.from_bytes(audio.readframes(1), 'little')

for i in range(570):
    transform = abs(fft(frames[128*i:128*i+127]))
    transform[0] = 0
    transform = transform/max(transform)
    # transform

    last_audio.append(transform)


print(last_audio[207])
im = Image.new('L', (570, 127))
for i in range(570):
    for j in range(127):
        try:
            im.putpixel((i, j), int(255*last_audio[i][j]))
        except:
            im.putpixel((i, j), 0)
plt.imshow(im)

# original_audio = frames[128:255]
# transform = fft(original_audio)
# transform[0] = 0
# transform = transform/max(abs(transform))
# reconstructed_audio = ifft(transform)
# fig, axs = plt.subplots(2, 1)
# axs[0].plot(original_audio)
# axs[0].set_ylabel('Original Frame')
# axs[1].plot(reconstructed_audio)
# axs[1].set_ylabel('Reconstructed Frame')

plt.show()
