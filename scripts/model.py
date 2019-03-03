from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
import random

import os
import pathlib


trainingPath = '../slices/training data'
testPath = '../slices/test data'
validationPath = '../slices/validation data'

training_image_paths = []
training_labels = []
validation_image_paths = []
validation_labels = []

def getPaths(source, array):
    for root, dirs, files in os.walk(source):
        for filename in files:
            path = root+'/'+filename
            array.append(path)
    random.shuffle(array)


genres = ['blues', 'rock', 'jazz', 'reggae', 'disco', 'pop', 'hiphop','country', 'metal', 'classical']
label_names = sorted(genres)

label_to_index = dict((name, index) for index,name in enumerate(label_names))


def getLabels(source, array):
    for path in source:
        path = path.split('/')
        if '.DS_Store' != path[3]:
            array.append(label_to_index[path[3]])

getPaths(trainingPath, training_image_paths)
getLabels(training_image_paths, training_labels)
getPaths(validationPath, validation_image_paths)
getLabels(validation_image_paths, validation_labels)


model = Sequential()
model.add(Conv2D(64, (5,5), activation='relu', input_shape=(256,256,3)))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (5,5), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(10, activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy',
        metrics=['accuracy'])


model.fit(training_image_paths, training_labels,
        validation_data=(validation_image_paths, validation_labels), epochs=3)
