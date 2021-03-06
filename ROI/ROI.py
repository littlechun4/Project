#!usr/bin/python
# -*- coding: utf-8 -*-
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np

class ROI:
    def __init__(self, view):
        self.rois = []
        self.view = view

    def setROI(self, shape):
        make = [pg.LineROI, pg.RectROI]
        roi = None
        if shape == 0:
            roi = pg.LineROI([0, 60], [20, 80], width=1, pen=(1,9))
        elif shape == 1:
            roi = pg.RectROI([20, 20], [20, 20], pen=(0,9))
        else:
            roi = pg.CircleROI([80, 50], [20, 20], pen=(4,9))
        self.rois.append(roi)
        self.view.addItem(roi)

    def getROIList(self):
        return self.rois


if __name__ == "__main__":
    arr = np.ones((100, 100), dtype=float)
    arr[45:55, 45:55] = 0
    arr[25, :] = 5
    arr[:, 25] = 5
    arr[75, :] = 5
    arr[:, 75] = 5
    arr[50, :] = 10
    arr[:, 50] = 10
    arr += np.sin(np.linspace(0, 20, 100)).reshape(1, 100)
    arr += np.random.normal(size=(100,100))

    app = QtGui.QApplication([])
    win = pg.GraphicsWindow(size=(800, 800), border=True)
    win.setWindowTitle('ROI test window')
    w1 = win.addLayout(row=0, col=0)
    v1a = w1.addViewBox(row=1, col=0, lockAspect=True)
    v1b = w1.addViewBox(row=2, col=0, lockAspect=True)
    img1a = pg.ImageItem(arr)
    v1a.addItem(img1a)
    img1b = pg.ImageItem()
    v1b.addItem(img1b)
    roia = ROI(v1a)
    roia.setROI(0)
    roia.setROI(1)
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
