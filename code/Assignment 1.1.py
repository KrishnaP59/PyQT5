# 1. plot a graph considering parameter individually
# figure 1 : College rank and Full time

import sys
import pandas as pd
import matplotlib

matplotlib.use('QT5Agg')
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.center()
        grid = QtWidgets.QGridLayout()
        widget = QtWidgets.QWidget(self)
        self.setCentralWidget(widget)
        widget.setLayout(grid)

    def plot(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        self.df.plot(x='Rank', y='Full_time')
        self.canvas.draw()

    def getCSV(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'file.csv')
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