#!usr/bin/python
# -*- coding: utf-8 -*-
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np


class ROIController:
    '''ROI 관리를 위한 클래스'''
    def __init__(self, ui):
        self.roi_lst = []
        self.ui = ui
        self.widget_lst = ui.plotwidget_lst

    def setROI(self, shape, rect=((10, 10), (20, 20))):
        '''ROI 추가를 위한 메서드. 좌상, 우하 좌표와, 모양을 인자로 받아
        선형, 사각형, 다선형, 삼각형, 원형의 ROI를 추가한다'''
        make = [pg.LineROI, pg.RectROI]
        roi_lst = []
        roi_id = len(self.roi_lst)

        def update(roi):
            '''ROI에 변화가 생겼을 대에 이를 다른 뷰에 적용시킨다'''
            state = roi.saveState()
            for r in self.roi_lst[roi_id]:
                r.setAngle(state['angle'], update=False)
                r.setPos(state['pos'], update=False)
                r.setSize(state['size'], update=False)

        def clicked(roi):
            '''ROI 우클릭 시에 팝업 윈도우를 보여준다'''
            ROIPopup(roi, self.ui)
            print "clicked"

        (x1, y1), (x2, y2) = rect
        x = min(x1, x2)
        y = min(y1, y2)
        xlen = abs(x1 - x2)
        ylen = abs(y1 - y2)

        for widget in self.widget_lst:
            if shape == 0:
                roi = pg.LineROI([x1, y1], [x2, 2 * y1 - y2],
                        width=0, pen=(1, 9))
            elif shape == 1:
                roi = pg.RectROI([x, y], [xlen, ylen], pen=(3, 9))
            elif shape == 2:
                roi = pg.PolyLineROI([[x, y + ylen], [x + xlen / 4, y],
                    [x + xlen / 2, y + ylen], [x + xlen * 3 / 4, y],
                    [x + xlen, y + ylen]], closed=False, pen=(5, 9))
            elif shape == 3:
                roi = pg.PolyLineROI([[x, y], [x + xlen / 4, y + ylen],
                    [x + xlen / 2, y], [x + xlen * 3 / 4, y + ylen],
                    [x + xlen, y]], closed=False, pen=(7, 9))
            elif shape == 4:
                roi = pg.PolyLineROI([[x, y], [x + xlen / 2, y + ylen],
                    [x + xlen, y]], closed=True, pen=(9, 9))
            elif shape == 5:
                roi = pg.EllipseROI([x, y], [xlen, ylen], pen=(4, 9))
            else:
                raise Exception("Shape unbound")

            # 시그널 연결
            roi.sigRegionChanged.connect(update)
            roi.setAcceptedMouseButtons(QtCore.Qt.RightButton)
            roi.sigClicked.connect(clicked)
            if shape == 2 or shape == 3 or shape == 4:
                for seg in roi.segments:
                    seg.sigRegionChanged.connect(update)
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


class ROIPopup(QtGui.QWidget):
    '''팝업 윈도우 위젯 클래스'''
    def __init__(self, roi, ui):
        QtGui.QWidget.__init__(self)
        self.roi = roi
        self.ui = ui
        self.initUI()

    def initUI(self):
        self.remove = QtGui.QPushButton('  Remove  ', self)
        self.removeall = QtGui.QPushButton('Remove All', self)

        self.remove.move(10, 5)
        self.removeall.move(10, 35)

        self.remove.clicked.connect(self.removePushed)
        self.removeall.clicked.connect(self.removeAllPushed)
        self.setGeometry(QtCore.QRect(600, 300, 110, 70))
        self.show()
        self.exec_()

    def removePushed(self):
        self.ui.removeROIByObj(self.roi)
        self.close()

    def removeAllPushed(self):
        self.ui.removeROIAll()
        self.close()
