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

numTracks = [0,0,0,0,0,0,0,0,0,0]
numCorrect = [0,0,0,0,0,0,0,0,0,0]

for root, dirs, files in os.walk("../wholepngs/validation"):
    for file in files:
        if file.endswith(".png"):
            img = cv2.imread(file)
            splitten = root.split('/')
            if splitten[3] == genres[0]:
                trackingIndex = 0
            elif splitten[3] == genres[1]:
                trackingIndex = 1
            elif splitten[3] == genres[2]:
                trackingIndex = 2
            elif splitten[3] == genres[3]:
                trackingIndex = 3
            elif splitten[3] == genres[4]:
                trackingIndex = 4
            elif splitten[3] == genres[5]:
                trackingIndex = 5
            elif splitten[3] == genres[6]:
                trackingIndex = 6
            elif splitten[3] == genres[7]:
                trackingIndex = 7
            elif splitten[3] == genres[8]:
                trackingIndex = 8
            elif splitten[3] == genres[9]:
                trackingIndex = 9

            numTracks[trackingIndex] = numTracks[trackingIndex] + 1

            countArray = [0,0,0,0,0,0,0,0,0,0]

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
                resultindex = np.where(result == np.amax(result))
                index = resultindex[1]
                for j in range(0,10):
                    if index == j:
                        index2 = j
                    #print(resultindex[1])
                countArray[index2] = countArray[index2] + 1
            prediction = countArray.index(max(countArray))

            if prediciton == splitten[3]:
                numCorrect[trackingIndex] = numCorrect[trackingIndex] + 1
print(numTracks)
print(numCorrect)
