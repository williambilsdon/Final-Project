import PIL
from PIL import Image

from __future__ import absolute_import, division, print_function

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

import os

baseheight = 240

img = Image.open('blues_00000_2.png')
hpercent = (baseheight / float(img.size[1]))
wsize = int((float(img.size[0]) * float(hpercent)))
img = img.resize((128, 128), PIL.Image.ANTIALIAS)
img.save('test.png')
