#Use PyQtgraph
import sys
import mainGUI
from PySide.QtGui import *
from PySide.QtCore import *


import matplotlib
matplotlib.use('Agg')

from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps

class MainWindow(QMainWindow, mainGUI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # Filename
        self.filename = ""
        self.im = None

        self.setupUi(self)

        # File Menu Actions
        self.actionOpen.triggered.connect(self.open_file)

        # Edit Menu Actions
        self.actionHeatmap.triggered.connect(self.heatmap)
        self.actionRotate.triggered.connect(self.rotate)


    def open_file(self):
        fileDialog = QFileDialog(self)
        self.filename = fileDialog.getOpenFileName()[0]
        if self.filename:
            self.pixmap = QPixmap(self.filename)
            height, width = self.pixmap.height(), self.pixmap.width()
            # Reducing the file size to display
            factor = width / 480
            factor2 = height / 480
            if height > width:
                height /= factor2
                width /= factor2
            else:
                height /= factor
                width /= factor
            self.label.setGeometry(15, 15, width, height)
            self.label.setPixmap(self.pixmap.scaledToHeight(height))
            self.im = Image.open(self.filename)



    def heatmap(self):
        return self.im.transpose(Image.FLIP_LEFT_RIGHT).show()




    def rotate(self):
        print(self.im)
        if self.im:
            self.im.rotate(45).show()
        else:
            print("Can't call heatmap")



app = QApplication(sys.argv)
path = QDir.currentPath()
app.addLibraryPath(path)
form = MainWindow()
form.show()
app.exec_()