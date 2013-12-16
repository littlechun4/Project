# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class ScrollPopup(QtGui.QWidget):
    """
    Scroll Option을 선택했을 때 생성되는 팝업 오브젝트 정의
    """
    def __init__(self, ui):
        QtGui.QWidget.__init__(self)
        self.ui = ui
        self.initUI()

    def initUI(self):
        """
        팝업 UI를 셋업하는 함수
        """
        self.text1 = QtGui.QLabel(QtCore.QString('Speed: '), self)

        self.unit = QtGui.QComboBox(self)
        self.unit.addItem('sec')
        self.unit.addItem('ms')

        #스크롤속도가 1초보다 큰 경우에는 sec단위로 표시
        if(self.ui.velocity > 1):
            self.velocity = QtGui.QLineEdit(QtCore.QString(str(self.ui.velocity)), self)
            self.unit.setCurrentIndex(0)

        #스크롤 속도가 1초보다 작은 경우에는 ms단위로 표시
        else:
            self.velocity = QtGui.QLineEdit(QtCore.QString(str(self.ui.velocity*1000)), self)
            self.unit.setCurrentIndex(1)

        self.text3 = QtGui.QLabel(QtCore.QString('Level to Scroll: '), self)
        self.scroll_level = QtGui.QComboBox(self)
        self.scroll_level.addItem('1')
        self.scroll_level.addItem('2')
        self.scroll_level.addItem('3')
        self.scroll_level.addItem('4')
        self.scroll_level.addItem('5')
        self.scroll_level.addItem('6')
        self.scroll_level.addItem('7')
        self.scroll_level.addItem('8')
        self.scroll_level.setCurrentIndex(self.ui.scroll_level-1)

        self.ok = QtGui.QPushButton('OK', self)
        self.cancel = QtGui.QPushButton('Cancel', self)

        self.text1.move(30, 15)
        self.velocity.move(90, 15)
        self.unit.move(240, 15)

        self.text3.move(30, 60)
        self.scroll_level.move(130, 60)

        self.ok.move(60, 105)
        self.cancel.move(150, 105)

        #버튼 이벤트 함수 연결
        self.ok.clicked.connect(self.okPushed)
        self.cancel.clicked.connect(self.cancelPushed)

        self.setGeometry(QtCore.QRect(100, 100, 300, 150))
        self.show()

    def okPushed(self):
        """
        OK버튼이 눌렸을 때 값을 저장하고 팝업을 닫는다.
        """
        self.ui.velocity = float(self.velocity.text())
        self.ui.scroll_level = self.scroll_level.currentIndex() + 1

        if(self.unit.currentIndex()==1):
            self.ui.velocity/=1000

        self.close()

    def cancelPushed(self):
        """
        Cancel버튼이 눌렸을 때 값을 저장하지 않고 팝업을 닫는다.
        """
        self.close()

