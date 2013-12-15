# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import pyqtgraph.parametertree.parameterTypes as pTypes

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class ROIParameter(pTypes.GroupParameter):
    '''Control Panel에 ROI를 추가/제거하기 위한 클래스이다.'''
    
    def __init__(self, **opts):
        opts['type'] = 'group'
        pTypes.GroupParameter.__init__(self, **opts)
        self.roi_num = 0
        self.toshape = ['Line', 'Rectangle', 'W', 'M', 'Triangle', 'Ellipse']
    
    def addROI(self, x_pos, shape):
        '''ROI의 위치와 모양 정보를 Control Panel에 추가하는 메서드이다.'''

        self.addChild({'name': 'ROI' + str(self.roi_num), 'type': 'group', 'children': [
            {'name': 'X-Position', 'type': 'str', 'value': x_pos, 'readonly': True},
            {'name': 'Shape', 'type': 'str', 'value': self.toshape[shape], 'readonly': True}
        ]})
        self.roi_num += 1
        return self.roi_num - 1
       
    def restoreROI(self, x_pos, num, shape):
        '''OPEN 시에 ROI의 정보를 복원하는 메서드이다.'''
        self.addChild({'name': 'ROI' + str(num), 'type': 'group', 'children': [
            {'name': 'X-Position', 'type': 'str', 'value': x_pos, 'readonly': True},
            {'name': 'Shape', 'type': 'str', 'value': self.toshape[shape], 'readonly': True}
        ]})
        self.roi_num = num + 1
    
    def removeROI(self, name):
        for child in self.children():
            if child.name() == name:
                self.removeChild(child) 

    def removeROIAll(self):
        self.clearChildren()

