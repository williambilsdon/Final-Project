from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential, load_model
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.callbacks import ModelCheckpoint
from keras.layers.normalization import BatchNormalization
from keras.preprocessing import image
import numpy as np
import operator
from pydub import AudioSegment as audiosegment
from scipy.io import wavfile as wav
import matplotlib.pyplot as plt

import random
import cv2
import os

imageX = 3200
numSlices = 10
xStride = imageX/numSlices
xPos = 0
newX = int(xPos) + int(xStride)

genres = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']

def isBigger(curNum, nextNum):
    if curNum < nextNum:
        predNum = nextNum
    print(curNum)
    print(nextNum)


model = Sequential()
model = load_model('130319_1_Model.h5')
model.load_weights('130319_1_Weights.h5')

countArray = [0,0,0,0,0,0,0,0,0,0]

genreCountDict = dict(zip(genres,countArray))

values = [0,0,0,0,0,0,0,0,0]

imgDims = 256

file = audiosegment.from_mp3('testing.mp3')

    #check if mp3 is mono audio
if file.channels != 1:
    file = file.set_channels(1)

    #save new mono file as a wav file
    file.export('holder.wav', format="wav")


    frequency_rate, data = wav.read('holder.wav', 'r')
    fig, ax = plt.subplots(1)
    fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
    ax.axis('off')
    pxx, frequency, bins, im = plt.specgram(x=data, Fs = frequency_rate, cmap = 'plasma', NFFT = 1024)
    plt.ylim([0, 10000])
    ax.axis('off')
    fig.savefig('010030.png', dpi=500, frameon='false')
    plt.close()

    os.remove('holder.wav')

img = cv2.imread('010030.png')
for i in range(0,10):
    slice = img[0:2400, int(xPos):int(newX)]
    xPos += xStride
    newX += xStride
    cv2.imwrite(('temp.png'), slice)
    #image = cv2.imread('temp.png')
    #os.remove('temp.png')

    test_image = image.load_img('temp.png', target_size=(imgDims, imgDims))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)


    result = model.predict(test_image, batch_size=1)
    print(result)

# for root, dirs, files in os.walk('../wholepngs'):
#     for filename in files:
#         predictions = []
#         print(filename)
#
#         imageX = 3200
#         numSlices = 10
#         xStride = imageX/numSlices
#         xPos = 0
#         newX = int(xPos) + int(xStride)
#         if filename != '.DS_Store':
#             img = cv2.imread(root + '/' + filename)
#             print('new')
#             for i in range(0,10):
#                 slice = img[0:2400, int(xPos):int(newX)]
#
#                 xPos += xStride
#                 newX += xStride
#
#                 cv2.imwrite(('temp.png'), slice)
#                 image = cv2.imread('temp.png')
#                 os.remove('temp.png')
#
#                 image = cv2.resize(image, (256, 256))
#                 image = image.astype("float") / 255.0
#                 image = img_to_array(image)
#                 image = np.expand_dims(image, axis=0)
#                 #proba = model.predict(image)[0]
#                 #idx = np.argmax(proba)
#                 #prediction = model.predict_classes(image)
#                 prediction = model.predict(image)[0]
#                 pred = prediction
#
#                 predID = 0
#                 for i in range(0,9):
#                     values[i] = pred[i]
#                 #    print(i)
#                 #    if pred[predID] < pred[i]:
#                 #        predID = i
#                 #    print(predID)
#
#                 print(values)
#
#                 maxNum = max(values)
#                 print(maxNum)
#
#                 #for i in range(0, 9):
#
#
#
#
#
#                 predictions.append(predID)
#                 print(predictions)
#
#             genreID = np.bincount(predictions).argmax()
#             print(genres[genreID])




print(predictions)


print(genreGuess)
