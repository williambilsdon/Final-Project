from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.callbacks import ModelCheckpoint
from keras.layers.normalization import BatchNormalization

import random

import os

import PIL
from PIL import Image

trainingPath = '../slices/training'
validationPath = '../slices/validation'



train_datagen = ImageDataGenerator(rescale=1./255)

test_datagen = ImageDataGenerator(rescale=1./255)

model = Sequential()
model.add(Conv2D(32, (2,2), activation='relu', input_shape=(256,256,3)))
#model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (2,2), activation='relu'))
#model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(64, (2,2), activation = 'relu'))
#model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(128, (2,2), activation = 'relu'))
#model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(256, (2,2), activation = 'relu'))
#model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2)))


#model.add(Conv2D(256, (2,2), activation = 'relu'))
#model.add(MaxPooling2D(pool_size=(2,2)))

#model.add(Conv2D(512, (2,2), activation = 'relu'))

model.add(Flatten())
model.add(Dense(512))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))

model.compile(optimizer='adam', loss='mean_squared_error',
        metrics=['accuracy'])

train_generator = train_datagen.flow_from_directory(
        trainingPath,
        target_size=(256, 256),
        batch_size=100,
        class_mode='categorical',
        shuffle = True)

validation_generator = test_datagen.flow_from_directory(
        validationPath,
        target_size=(256, 256),
        batch_size=100,
        class_mode='categorical')

filepath = "model.h5"
checkpoint = ModelCheckpoint(filepath, monitor='val_loss', verbose=1, save_best_only=True, mode='auto')
callbacks_list = [checkpoint]

model.fit_generator(
        train_generator,
        steps_per_epoch=9401/100,
        epochs=100,
        validation_data=validation_generator,
        validation_steps=4029/100)

model.save_weights('130319_1_Weights.h5')
model.save('130319_1_Model.h5')
