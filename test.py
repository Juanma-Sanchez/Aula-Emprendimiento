from PIL import Image

from audio_format import AudioFormatter

image = AudioFormatter.format('audio_folder\idiomas-2.mp3')
image.show()
