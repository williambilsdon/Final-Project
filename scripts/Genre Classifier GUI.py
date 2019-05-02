import sys, os, random, cv2
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PIL import Image
from pydub import AudioSegment as audiosegment
from scipy.io import wavfile as wav
import matplotlib.pyplot as plt
from resizeimage import resizeimage
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential, load_model
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.callbacks import ModelCheckpoint
from keras.layers.normalization import BatchNormalization
from keras.preprocessing import image
import numpy as np


fileN = ""
fullSpectrograms = []
smallSpectrograms = []
classification = []
trackNames = []

def createspecgram(self):
    global fileN
    file = audiosegment.from_mp3(fileN)

    trackNames.append(fileN)

    if file.channels != 1:
        file = file.set_channels(1)

        #save new mono file as a wav file
        file.export('holder.wav', format="wav")

        fullDest = 'fullsize' + str(self.i) + '.png'
        smallDest = 'track'+ str(self.i) + '.png'

        frequency_rate, data = wav.read('holder.wav', 'r')
        fig, ax = plt.subplots(1)
        fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
        ax.axis('off')
        pxx, frequency, bins, im = plt.specgram(x=data, Fs = frequency_rate, cmap = 'plasma', NFFT = 1024)
        plt.ylim([0, 10000])
        ax.axis('off')
        fig.savefig(smallDest, dpi=500, frameon='false')
        fig.savefig(fullDest, dpi=500, frameon='false')
        plt.close()

        os.remove('holder.wav')

        fullSpectrograms.append(fullDest)
        smallSpectrograms.append(smallDest)
        img = Image.open(smallDest)

        resize = resizeimage.resize_cover(img, [410, 200])
        resize.save(smallDest, img.format)

def showimage(self):
    self.label.setPixmap(QPixmap(smallSpectrograms[self.imageIndex]))
    self.label.repaint()

def updateGenreText(self):
    self.genreLabel.setText(classification[self.imageIndex])
    width = self.genreLabel.fontMetrics().boundingRect(self.genreLabel.text()).width()
    self.genreLabel.move((215-(width/2)), 150)
    self.genreLabel.repaint()

def showTrackName(self):
    self.trackLabel.setText(trackNames[self.imageIndex])
    width = self.trackLabel.fontMetrics().boundingRect(self.trackLabel.text()).width()
    self.trackLabel.move((215-(width/2)), 50)
    self.trackLabel.repaint()

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Music Genre Classifier'
        self.left = 10
        self.top = 10
        self.width = 430
        self.height = 280
        self.imageIndex = 0
        self.genre = ""
        self.i = 0
        self.initUI()

    def initUI(self):
        newFont = QFont("serif", 10)
        self.trackLabel = QLabel(self)
        self.trackLabel.setFont(newFont)
        self.trackLabel.setGeometry(10,10,430,20)
        self.trackLabel.move(10, 50)

        self.setFixedSize(self.width, self.height)
        self.btnSelect = QPushButton("Select Song", self)
        self.btnSelect.resize(self.btnSelect.sizeHint())
        self.btnSelect.clicked.connect(self.getfile)
        self.btnSelect.move(10,10)

        self.btnGenerate = QPushButton("Classify Spectrogram", self)
        self.btnGenerate.resize(self.btnGenerate.sizeHint())
        self.btnGenerate.clicked.connect(self.classify)
        self.btnGenerate.move(255,10)

        self.label = QLabel(self)
        self.label.setGeometry(10,10,410, 200)
        self.label.move(10, 70)
        self.label.setStyleSheet("QLabel {background-color: #e6e6e6;}")

        self.genreLabel = QLabel(self)

        self.genreLabel.setText(self.genre)
        newFont = QFont("serif", 20, QFont.Bold)
        self.genreLabel.setFont(newFont)
        self.genreLabel.setGeometry(10,10,140, 40)
        width = self.genreLabel.fontMetrics().boundingRect(self.genreLabel.text()).width()
        self.genreLabel.move((215-(width/2)), 150)

        self.specImageChangerRight = QPushButton(">",self)
        newFont = QFont("serif", 20, QFont.Bold)
        self.specImageChangerRight.setFont(newFont)
        self.specImageChangerRight.setGeometry(10,10,40,40)
        self.specImageChangerRight.move(380, 150)
        self.specImageChangerRight.clicked.connect(self.imgchangeRight)
        self.specImageChangerRight.hide()

        self.specImageChangerLeft = QPushButton("<",self)
        newFont = QFont("serif", 20, QFont.Bold)
        self.specImageChangerLeft.setFont(newFont)
        self.specImageChangerLeft.setGeometry(10,10,40,40)
        self.specImageChangerLeft.move(10, 150)
        self.specImageChangerLeft.clicked.connect(self.imgchangeLeft)
        self.specImageChangerLeft.hide()


        self.show()

    def imgchangeLeft(self):
        self.imageIndex = self.imageIndex - 1
        if self.specImageChangerRight.isVisible() is False:
            self.specImageChangerRight.show()

        if self.imageIndex == 0:
            self.specImageChangerLeft.hide()

        showimage(self)
        showTrackName(self)
        try:
            updateGenreText(self)
        except:
            print("Not classified")

    def imgchangeRight(self):
        self.imageIndex = self.imageIndex + 1
        if self.specImageChangerLeft.isVisible() is False:
            self.specImageChangerLeft.show()
        if (self.imageIndex + 1) == len(smallSpectrograms):
            self.specImageChangerRight.hide()
        showimage(self)
        showTrackName(self)
        try:
            updateGenreText(self)
        except:
            print("Not classified")

    def getfile(self):
        self.genreLabel.setText("")
        self.genreLabel.repaint()
        fileNames = QFileDialog.getOpenFileNames(self, 'Open File')
        #print(fileName[0])
        global fileN
        length = len(fileNames[0])
        j = 0
        while j < length:
            fileN = fileNames[0][j]
            createspecgram(self)
            self.i = self.i +1
            j = j + 1

        showimage(self)
        showTrackName(self)
        if len(smallSpectrograms) > 1:
            self.specImageChangerRight.show()




    def classify(self):
        for fullspec in fullSpectrograms:
            imageX = 3200
            numSlices = 10
            xStride = imageX/numSlices
            xPos = 0
            newX = int(xPos) + int(xStride)
            prediction = 0

            imgDims = 256

            genres = ['Blues', 'Classical', 'Country', 'Disco', 'Hip-Hop', 'Jazz', 'Metal', 'Pop', 'Reggae', 'Rock']

            model = Sequential()
            model = load_model('130319_1_Model.h5')
            model.load_weights('130319_1_Weights.h5')

            countArray = [0,0,0,0,0,0,0,0,0,0]

            img = cv2.imread(fullspec)
            for k in range(0,10):
                slice = img[0:2400, int(xPos):int(newX)]
                xPos += xStride
                newX += xStride
                cv2.imwrite(('temp.png'), slice)

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

                os.remove('temp.png')

            prediction = countArray.index(max(countArray))
            os.remove(fullspec)

            self.genre = genres[prediction]
            classification.append(self.genre)
            print(classification)
            print(self.imageIndex)
            self.genreLabel.setText(classification[self.imageIndex])
            width = self.genreLabel.fontMetrics().boundingRect(self.genreLabel.text()).width()
            self.genreLabel.move((215-(width/2)), 150)
            self.genreLabel.repaint()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
