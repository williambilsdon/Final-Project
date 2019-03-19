from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential, load_model
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.callbacks import ModelCheckpoint
from keras.layers.normalization import BatchNormalization
from keras.preprocessing.image import img_to_array
import numpy as np

import random
import cv2
import os

imageX = 3200
numSlices = 10
xStride = imageX/numSlices
xPos = 0
newX = int(xPos) + int(xStride)

genres = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']

image_path = 'pop.00056.png'
img = cv2.imread(image_path)


model = load_model('130319_1_Model.h5')

predictions = []

for i in range(0,10):
    slice = img[0:2400, int(xPos):int(newX)]

    cv2.imwrite(('temp.png'), slice)
    image = cv2.imread('temp.png')
    image = cv2.resize(image, (256, 256))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    result = model.predict(image)[0]
    print(result)
    maxNum = max(result)
    id = np.where(result == maxNum)

    predictions.append(maxNum)

    print(maxNum)

    xPos += xStride
    newX += xStride

print(predictions)

wholePred = np.bincount(predictions).argmax()
genreGuess = genres[wholePred]

print(genreGuess)
