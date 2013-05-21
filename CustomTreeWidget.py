# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from pyqtgraph.parametertree import ParameterTree

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class MyTreeWidget(ParameterTree):
    def __init__(self, parent=None):
        super(MyTreeWidget, self).__init__(parent)
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setHeaderLabels(["Parameter"])
        self.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)

        self.actionRemove = QtGui.QAction('remove', self)
        self.actionRemoveAll = QtGui.QAction('remove all', self)

        self.actionRemove.triggered.connect(self.remove)
        self.actionRemoveAll.triggered.connect(self.remove_all)

        """
        우클릭하면 뜨는 메뉴들 설정
        """
        self.popMenu = QtGui.QMenu(self)
        self.popMenu.addAction(self.actionRemove)
        self.popMenu.addAction(self.actionRemoveAll)

        # ROI
        self.actionRemoveROI = QtGui.QAction('remove', self)
        self.actionRemoveROIAll = QtGui.QAction('remove all', self)

        self.actionRemoveROI.triggered.connect(self.removeROI)
        self.actionRemoveROIAll.triggered.connect(self.removeROI_all)

        self.popMenuROI = QtGui.QMenu(self)
        self.popMenuROI.addAction(self.actionRemoveROI)
        self.popMenuROI.addAction(self.actionRemoveROIAll)

        #self.main_window = main_window

    """
    더블 클릭시 왼쪽 버튼이면 스크롤을 호출
    """
    def mouseDoubleClickEvent(self, event):
        super(MyTreeWidget, self).mouseDoubleClickEvent(event)
        name = super(MyTreeWidget, self).itemAt(event.pos()).text(0)
        if event.button() == QtCore.Qt.LeftButton:
            if name == "X-Position" or name == "Y-Position" or name == "Type" or name == "Shape":
                self.main_window.parameterScroll(super(MyTreeWidget, self).itemAt(event.pos()).parent().text(0))

    """
    클릭 시 우측 버튼이면 삭제 팝업 메뉴 띄움
    """
    def mousePressEvent(self, event):
        super(MyTreeWidget, self).mousePressEvent(event)

        if event.button() == QtCore.Qt.RightButton:
            if super(MyTreeWidget, self).itemAt(event.pos()).text(0) == "Arrow":
                pass
            elif super(MyTreeWidget, self).itemAt(event.pos()).text(0).contains("Arrow"):
                self.pos = event.pos()
                self.popMenu.exec_(event.globalPos())
            elif super(MyTreeWidget, self).itemAt(event.pos()).text(0) == "ROI":
                pass
            elif super(MyTreeWidget, self).itemAt(event.pos()).text(0).contains("ROI"):
                self.pos = event.pos()
                self.popMenuROI.exec_(event.globalPos())

    """
    parameter에서 arrow를 삭제함
    """
    def remove(self, arrow_name):
        self.main_window.removeArrow(super(MyTreeWidget, self).itemAt(self.pos))
        #super(MyTreeWidget, self).itemAt(self.pos).parent().removeChild(super(MyTreeWidget, self).itemAt(self.pos))

    """
    화살표 전부 삭제
    """
    def remove_all(self):
        self.main_window.removeArrowAll()

    # ROI
    def removeROI(self):
        self.main_window.removeROIByItem(super(MyTreeWidget, self).itemAt(self.pos))

    def removeROI_all(self):
        self.main_window.removeROIAll()

    def setMainWindow(self, main):
        self.main_window = main
