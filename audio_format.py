import wave

from numpy.fft import fft
from PIL import Image


class AudioFormatter:
    @staticmethod
    def format(frames=[]) -> Image:
        audio_matrix = []

        for i in range(570):
            dft = abs(fft(frames[128 * i:128 * i + 127]))
            transform = dft[0:64]
            transform[0] = 0
            transform = transform / max(transform)
            audio_matrix.append(transform)

        audio_image = Image.new('L', (570, 65))

        for i in range(570):
            for j in range(65):
                try:
                    audio_image.putpixel((i, j), int(255 * audio_matrix[i][j]))
                except:
                    audio_image.putpixel((i, j), 0)

        return audio_image
