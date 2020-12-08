# Bar graph between college rank ,college jobs and non-college jobs
# figure 1 : college rank and College jobs

import sys
import pandas as pd
import matplotlib

matplotlib.use('QT5Agg')
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import pyqtgraph as pg
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 300, 1000, 600)
        self.center()
        grid = QtWidgets.QGridLayout()
        widget = QtWidgets.QWidget(self)
        self.setCentralWidget(widget)
        widget.setLayout(grid)
        # Import CSV Button
        btn1 = QtWidgets.QPushButton('Import CSV', self)
        btn1.resize(btn1.sizeHint())
        btn1.clicked.connect(self.getCSV)
        grid.addWidget(btn1, 1, 0)

        self.figure = plt.figure(figsize=(5, 5))
        self.canvas = FigureCanvas(self.figure)
        grid.addWidget(self.canvas, 2, 0, 1, 2)

        btn2 = QtWidgets.QPushButton('Plot', self)
        btn2.resize(btn2.sizeHint())
        btn2.clicked.connect(self.create_bar)
        grid.addWidget(btn2, 1, 1)
        self.show()

    def create_bar(self):
        x = self.df['Rank']
        y = self.df['College_jobs']
        plot = pg.plot()
        bargraph = pg.BarGraphItem(x=x, height=y, width=0.6, brush='b')
        plot.addItem(bargraph)
        plot.patch.set_facecolor('black')

    def getCSV(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'file3.csv')
        if filePath != "":
            print("Direccion", filePath)
            self.df = pd.read_csv(str(filePath))

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


def main():
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()