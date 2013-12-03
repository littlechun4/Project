import numpy as np
import pyqtgraph as pg
import pandas as pd
from pyqtgraph.Qt import QtGui, QtCore

from CustomGraph import CustomGraph

app = QtGui.QApplication([])
mw = QtGui.QMainWindow()
mw.resize(800, 800)
w = pg.PlotWidget()
mw.setCentralWidget(w)
mw.show()
rd = pd.read_csv('./synth.csv', index_col=[0], header=None, names=['dt', 'value'])

lst = []

for val in rd.value:
	lst += [val]

g = CustomGraph(lst)
w.addItem(g)

#g = w.plot(y=lst)

if __name__ == '__main__':
	import sys
	if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
		QtGui.QApplication.instance().exec_()
