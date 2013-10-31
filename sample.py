from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
import pandas as pd

rd = pd.read_csv('./synth.csv', index_col=[0], header=None, names=['dt', 'value'])

app = QtGui.QApplication([])
win = pg.GraphicsWindow(title = "Basic")

lst = []

for val in rd.value:
	lst += [val]

p1 = win.addPlot(title = "Plot" , y = lst)


if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
