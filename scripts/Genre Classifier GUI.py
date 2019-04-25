import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QToolTip, QPushButton
from PyQt5.QtGui import QIcon


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file dialogs - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        btn = QPushButton("Select Song", self)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.getfile)
        btn.move(150,150)

        self.show()


    def getfile(self):
        fileName = QFileDialog.getOpenFileName(self, 'Open File')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
