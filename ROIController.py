#!usr/bin/python
# -*- coding: utf-8 -*-
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np

class ROIController:
    def __init__(self, widget_lst):
        self.roi_lst = []
        self.widget_lst = widget_lst
      
    def setROI(self, shape, rect=((10, 10), (20,20))):
        make = [pg.LineROI, pg.RectROI]
        roi_lst = []
        roi_id = len(self.roi_lst)
        def update(roi):
            state = roi.saveState()
            for r in self.roi_lst[roi_id]:
                r.setAngle(state['angle'], update=False)
                r.setPos(state['pos'], update=False)
                r.setSize(state['size'], update=False)

        (x1, y1), (x2, y2) = rect
        x = min(x1, x2)
        y = min(y1, y2)
        xlen = abs(x1-x2)
        ylen = abs(y1-y2)

        for widget in self.widget_lst:
           if shape == 0:
               roi = pg.LineROI([x1, y1], [x2, y2], width=1, pen=(1,9))
           elif shape == 1:
               roi = pg.RectROI([x, y], [xlen, ylen], pen=(3,9))
           elif shape == 2:
               roi = pg.PolyLineROI([[x, y+ylen], [x+xlen/4, y], [x+xlen/2, y+ylen], [x+xlen*3/4, y], [x+xlen, y+ylen]], closed=False, pen=(5,9))
           elif shape == 3:
               roi = pg.PolyLineROI([[x, y], [x+xlen/4, y+ylen], [x+xlen/2, y], [x+xlen*3/4, y+ylen], [x+xlen, y]], closed=False, pen=(7,9))
           elif shape == 4:
               roi = pg.PolyLineROI([[x, y], [x+xlen/2, y+ylen], [x+xlen, y]], closed=True, pen=(9,9))
           else:
               roi = pg.CircleROI([80, 50], [20, 20], pen=(4,9))
           roi.sigRegionChanged.connect(update)
           widget.addItem(roi)
           roi_lst.append(roi)
        self.roi_lst.append(roi_lst)
        return x
    
    def removeROI(self, index):
        for (roi, widget) in zip(self.roi_lst[index], self.widget_lst):
            widget.removeItem(roi)
        self.roi_lst[index] = []

    def removeAll(self):
        for index in xrange(len(self.roi_lst)):
            self.removeROI(index)

    def getROIList(self):
        return self.roi_lst
