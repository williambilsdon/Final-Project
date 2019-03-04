from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
import random

import os

import PIL
from PIL import Image

trainingPath = '../slices/training data'
testPath = '../slices/test data'
validationPath = '../slices/validation data'



train_datagen = ImageDataGenerator(rescale=1./255)

test_datagen = ImageDataGenerator(rescale=1./255)

model = Sequential()
model.add(Conv2D(32, (3,3), activation='relu', input_shape=(256,256,3)))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(128, (3,3), activation = 'relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(256, (3,3), activation = 'relu'))
#model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(256))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy',
        metrics=['accuracy'])

train_generator = train_datagen.flow_from_directory(
        trainingPath,
        target_size=(256, 256),
        batch_size=100,
        class_mode='categorical')

validation_generator = test_datagen.flow_from_directory(
        validationPath,
        target_size=(256, 256),
        batch_size=100,
        class_mode='categorical')

model.fit_generator(
        train_generator,
        steps_per_epoch=9000/100,
        epochs=100,
        validation_data=validation_generator,
        validation_steps=1000/100,
        shuffle = True)

model.save_weights('firstTraining.h5')
