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

def createspecgram(self, i):
    global fileN
    file = audiosegment.from_mp3(fileN)

    if file.channels != 1:
        file = file.set_channels(1)

        #save new mono file as a wav file
        file.export('holder.wav', format="wav")

        fullDest = 'fullsize' + str(i) + '.png'
        smallDest = 'track'+ str(i) + '.png'

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

        print(fullSpectrograms)

        resize = resizeimage.resize_cover(img, [410, 200])
        resize.save(smallDest, img.format)

        #self.imageLink = "track.png"
        #self.showimage(self.imageLink)

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Music Genre Classifier'
        self.left = 10
        self.top = 10
        self.width = 430
        self.height = 280
        self.imageLink = ""
        self.genre = ""
        self.initUI()

    def initUI(self):
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

        #self.genreLabel.move(50,50)
        self.genreLabel.setText(self.genre)
        newFont = QFont("serif", 20, QFont.Bold)
        self.genreLabel.setFont(newFont)
        self.genreLabel.setGeometry(10,10,140, 40)
        width = self.genreLabel.fontMetrics().boundingRect(self.genreLabel.text()).width()
        self.genreLabel.move((215-(width/2)), 150)
        #self.genreLabel.setAlignment(Qt.AlignCenter)

        self.show()



    def getfile(self):
        self.genreLabel.setText("")
        self.genreLabel.repaint()
        fileNames = QFileDialog.getOpenFileNames(self, 'Open File')
        #print(fileName[0])
        global fileN
        i = 0
        print(fileNames)
        length = len(fileNames[0])
        while i < length:
            fileN = fileNames[0][i]
            print(fileNames[0][i])
            createspecgram(self, i)
            i = i +1



    def showimage(self,link):
        print(link)
        self.label.setPixmap(QPixmap(link))
        self.label.repaint()
        os.remove('track.png')


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
            for i in range(0,10):
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
            print(genres[prediction])
            os.remove(fullspec)

            self.genre = genres[prediction]
            self.genreLabel.setText(self.genre)
            width = self.genreLabel.fontMetrics().boundingRect(self.genreLabel.text()).width()
            self.genreLabel.move((215-(width/2)), 150)
            self.genreLabel.repaint()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
