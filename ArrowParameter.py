# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import pyqtgraph.parametertree.parameterTypes as pTypes

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class ArrowParameter(pTypes.GroupParameter):
    """ 
    화살표를 위한 별도의 parameter 클래스이다.
    최초에 num을 저장해서 화살표가 구분 표시를 위해 사용하며
    화살표 추가와 화살표 전부 삭제 기능을 제공한다.
    """
    def __init__(self, **opts):
        #super(ArrowParameter, self).__init__()
        opts['type'] = 'group'
        pTypes.GroupParameter.__init__(self, **opts)
        self.num = 0
 
    """
    화살표 추가의 경우 인자로 x, y, type을 받아서 각각의 정보를 arrow + number의 group아래 띄워준다.
    그리고 저장을 위해서 이름으로 사용했던 num을 넘겨준다.
    """
    def addArrow(self, x_pos, y_pos, arrow_type):
        self.addChild({'name': 'Arrow' + str(self.num), 'type': 'group', 'children': [
            {'name': 'X-Position', 'type': 'str', 'value': x_pos, 'readonly': True},
            {'name': 'Y-Position', 'type': 'int', 'value': y_pos, 'readonly': True},
            {'name': 'Type', 'type': 'int', 'value': arrow_type, 'readonly': True}
        ]})
        self.num += 1
        return self.num - 1

    """
    저장된 화살표를 복구할 때 사용하는 함수
    """
    def restoreArrow(self, x_pos, y_pos, num, arrow_type):
        self.addChild({'name': 'Arrow' + str(num), 'type': 'group', 'children': [
            {'name': 'X-Position', 'type': 'str', 'value': x_pos, 'readonly': True},
            {'name': 'Y-Position', 'type': 'int', 'value': y_pos, 'readonly': True},
            {'name': 'Type', 'type': 'int', 'value': arrow_type, 'readonly': True}
        ]})
        self.num = num + 1

    def removeArrow(self, name):
        child = self.children()
        for c in child:
            if c.name() == name:
                self.removeChild(c) 

    # 화살표 parameter를 모두 지움.
    def removeArrowAll(self):
        self.clearChildren()
