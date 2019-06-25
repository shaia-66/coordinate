from PIL import Image
import os

path = os.path.dirname(os.path.abspath("__file__")) + "画像のパスを指定"
img = Image.open(path)

width, height = 2040, 880
img = img.resize((width, height))
img.save(os.path.dirname(os.path.abspath("__file__")) + "結果の画像を置きたいパスを指定", dpi=(240, 240))
