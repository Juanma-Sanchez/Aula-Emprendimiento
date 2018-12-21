from pydub import AudioSegment
from numpy import fft
from PIL import Image
import numpy as np


class AudioFormatter:
    @staticmethod
    def format(filename=None) -> Image:
        AudioSegment.ffmpeg = None
        sound = AudioSegment.from_mp3(filename)
        samples = sound.get_array_of_samples()
        frames = [samples[i:i+127] for i in range(0, len(samples)//128, 128)]
        data = np.zeros((128, len(frames), 1), dtype=np.uint8)

        for i in range(0, len(frames)):
            data[:, i] = fft(frames[i])

        result = Image.fromarray(data)

        return result
