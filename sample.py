from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
import pandas as pd
import time
import datetime

rd = pd.read_csv('./synth.csv', index_col=[0], header=None, names=['dt', 'value'])
rd2 = pd.read_csv('./synth.csv', header=None, names=['dt', ''])

app = QtGui.QApplication([])
win = pg.GraphicsWindow(title = "Basic")

times = []
lst = []

for dt in rd2.dt:
	stamp = time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M:%S'))
	times += [stamp]


for val in rd.value:
	lst += [val]

p1 = win.addPlot(title="Plot" , x = times, y = lst)
lr = pg.LinearRegionItem([times[30000], times[70000]])
lr.setZValue(-10)
p1.addItem(lr)
p2 = win.addPlot(title="Region")
p2.plot(x=times, y=lst)
def updatePlot():
	p2.setXRange(*lr.getRegion(), padding=0)
def updateRegion():
	lr.setRegion(p2.getViewBox().viewRange()[0])
lr.sigRegionChanged.connect(updatePlot)
p2.sigXRangeChanged.connect(updateRegion)
updatePlot()

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
