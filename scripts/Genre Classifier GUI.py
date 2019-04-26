import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PIL import Image
from resizeimage import resizeimage


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Music Genre Classifier'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setFixedSize(self.width, self.height)
        btnSelect = QPushButton("Select Song", self)
        btnSelect.resize(btnSelect.sizeHint())
        btnSelect.clicked.connect(self.getfile)
        btnSelect.move(10,10)

        btnGenerate = QPushButton("Create Spectrogram", self)
        btnGenerate.resize(btnGenerate.sizeHint())
        btnGenerate.clicked.connect(self.createspecgram)
        btnGenerate.move(220,10)

        btnClassify = QPushButton("Classify", self)
        btnClassify.resize(btnGenerate.sizeHint())
        btnGenerate.clicked.connect(self.classify)
        btnClassify.move(470, 10)


        img = Image.open("/Users/williambilsdon/Desktop/Final-Project/scripts/010030.png")

        cover = resizeimage.resize_cover(img, [620, 200])
        cover.save("/Users/williambilsdon/Desktop/Final-Project/scripts/010030.png", img.format)

        pic = QLabel(self)
        pic.setGeometry(10, 10, 620, 200)
        pic.move(10,270)
        pixmap = QPixmap("010030.png")
        pic.setPixmap(pixmap)

        self.show()


    def getfile(self):
        fileName = QFileDialog.getOpenFileName(self, 'Open File')

    def createspecgram(self):
        print('hey')

    def classify(self):
        print('hello')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
