# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui2.ui'
#
# Created: Wed Dec  4 15:36:01 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

import pickle
from bisect import bisect_left, bisect_right
import time
from datetime import datetime

from PyQt4 import QtCore, QtGui
import pandas as pd
import pyqtgraph as pg
from pyqtgraph import PlotWidget
from pyqtgraph.parametertree import Parameter, ParameterTree, ParameterItem, registerParameterType
import pyqtgraph.parametertree.parameterTypes as pTypes

import BG_Popup
import Data_Popup
from ROIController import ROIController
from CustomGraph import CustomGraph, CustomAxis
from CustomTreeWidget import MyTreeWidget
from ScrollPopup import ScrollPopup
from ROIParameter import ROIParameter
from ArrowParameter import ArrowParameter

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(844, 833)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setMargin(4)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter_3 = QtGui.QSplitter(self.centralwidget)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.splitter = QtGui.QSplitter(self.splitter_3)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.treeWidget = MyTreeWidget(self.splitter)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget_2 = MyTreeWidget(self.splitter)
        self.treeWidget_2.setObjectName(_fromUtf8("treeWidget_2"))
        self.splitter_2 = QtGui.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.graphicsView_8 = PlotWidget(self.splitter_2, axisItems={'bottom':CustomAxis(orientation='bottom')})
        self.graphicsView_8.setObjectName(_fromUtf8("graphicsView_8"))
        self.graphicsView_7 = PlotWidget(self.splitter_2, axisItems={'bottom':CustomAxis(orientation='bottom')})
        self.graphicsView_7.setObjectName(_fromUtf8("graphicsView_7"))
        self.graphicsView_6 = PlotWidget(self.splitter_2, axisItems={'bottom':CustomAxis(orientation='bottom')})
        self.graphicsView_6.setObjectName(_fromUtf8("graphicsView_6"))
        self.graphicsView_5 = PlotWidget(self.splitter_2, axisItems={'bottom':CustomAxis(orientation='bottom')})
        self.graphicsView_5.setObjectName(_fromUtf8("graphicsView_5"))
        self.graphicsView_4 = PlotWidget(self.splitter_2, axisItems={'bottom':CustomAxis(orientation='bottom')})
        self.graphicsView_4.setObjectName(_fromUtf8("graphicsView_4"))
        self.graphicsView_3 = PlotWidget(self.splitter_2, axisItems={'bottom':CustomAxis(orientation='bottom')})
        self.graphicsView_3.setObjectName(_fromUtf8("graphicsView_3"))
        self.graphicsView_2 = PlotWidget(self.splitter_2, axisItems={'bottom':CustomAxis(orientation='bottom')})
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        self.graphicsView = PlotWidget(self.splitter_2, axisItems={'bottom':CustomAxis(orientation='bottom')})
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout.addWidget(self.splitter_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 844, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        self.menuLayout = QtGui.QMenu(self.menubar)
        self.menuLayout.setObjectName(_fromUtf8("menuLayout"))
        self.menuNumber_of_Graph_Windows = QtGui.QMenu(self.menuLayout)
        self.menuNumber_of_Graph_Windows.setObjectName(_fromUtf8("menuNumber_of_Graph_Windows"))
        self.menuScroll = QtGui.QMenu(self.menubar)
        self.menuScroll.setObjectName(_fromUtf8("menuScroll"))
        self.menuROI = QtGui.QMenu(self.menubar)
        self.menuROI.setObjectName(_fromUtf8("menuROI"))
        self.menuInsert_2 = QtGui.QMenu(self.menuROI)
        self.menuInsert_2.setObjectName(_fromUtf8("menuInsert_2"))
        self.menuArrow = QtGui.QMenu(self.menubar)
        self.menuArrow.setObjectName(_fromUtf8("menuArrow"))
        self.menuInsert = QtGui.QMenu(self.menuArrow)
        self.menuInsert.setObjectName(_fromUtf8("menuInsert"))
        self.menuBG_Fill = QtGui.QMenu(self.menubar)
        self.menuBG_Fill.setObjectName(_fromUtf8("menuBG_Fill"))
        self.menuData = QtGui.QMenu(self.menubar)
        self.menuData.setObjectName(_fromUtf8("menuData"))
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtGui.QToolBar("File", MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtGui.QToolBar("Layout", MainWindow)
        self.toolBar_2.setObjectName(_fromUtf8("toolBar_2"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        MainWindow.insertToolBarBreak(self.toolBar_2)
        self.toolBar_3 = QtGui.QToolBar("Scroll", MainWindow)
        self.toolBar_3.setObjectName(_fromUtf8("toolBar_3"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_3)
        MainWindow.insertToolBarBreak(self.toolBar_3)
        self.toolBar_4 = QtGui.QToolBar("ROI", MainWindow)
        self.toolBar_4.setObjectName(_fromUtf8("toolBar_4"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_4)
        MainWindow.insertToolBarBreak(self.toolBar_4)
        self.actionFile = QtGui.QAction(MainWindow)
        self.actionFile.setObjectName(_fromUtf8("actionFile"))
        self.action12 = QtGui.QAction(MainWindow)
        self.action12.setObjectName(_fromUtf8("action12"))
        self.action1 = QtGui.QAction(MainWindow)
        self.action1.setObjectName(_fromUtf8("action1"))
        self.action2 = QtGui.QAction(MainWindow)
        self.action2.setObjectName(_fromUtf8("action2"))
        self.action3 = QtGui.QAction(MainWindow)
        self.action3.setObjectName(_fromUtf8("action3"))
        self.action4 = QtGui.QAction(MainWindow)
        self.action4.setObjectName(_fromUtf8("action4"))
        self.action5 = QtGui.QAction(MainWindow)
        self.action5.setObjectName(_fromUtf8("action5"))
        self.action6 = QtGui.QAction(MainWindow)
        self.action6.setObjectName(_fromUtf8("action6"))
        self.action7 = QtGui.QAction(MainWindow)
        self.action7.setObjectName(_fromUtf8("action7"))
        self.action8 = QtGui.QAction(MainWindow)
        self.action8.setObjectName(_fromUtf8("action8"))
        self.actionStart = QtGui.QAction(MainWindow)
        self.actionStart.setObjectName(_fromUtf8("actionStart"))
        self.actionPause = QtGui.QAction(MainWindow)
        self.actionPause.setObjectName(_fromUtf8("actionPause"))
        self.actionResume = QtGui.QAction(MainWindow)
        self.actionResume.setObjectName(_fromUtf8("actionResume"))
        self.actionStop = QtGui.QAction(MainWindow)
        self.actionStop.setObjectName(_fromUtf8("actionStop"))
        self.actionSet_Scroll_Options = QtGui.QAction(MainWindow)
        self.actionSet_Scroll_Options.setObjectName(_fromUtf8("actionSet_Scroll_Options"))
        self.actionArrow_1 = QtGui.QAction(MainWindow)
        self.actionArrow_1.setObjectName(_fromUtf8("actionArrow_1"))
        self.actionArrow_2 = QtGui.QAction(MainWindow)
        self.actionArrow_2.setObjectName(_fromUtf8("actionArrow_2"))
        self.actionLine = QtGui.QAction(MainWindow)
        self.actionLine.setObjectName(_fromUtf8("actionLine"))
        self.actionRectangle = QtGui.QAction(MainWindow)
        self.actionRectangle.setObjectName(_fromUtf8("actionRectangle"))
        self.actionW = QtGui.QAction(MainWindow)
        self.actionW.setObjectName(_fromUtf8("actionW"))
        self.actionM = QtGui.QAction(MainWindow)
        self.actionM.setObjectName(_fromUtf8("actionM"))
        self.actionTriangle = QtGui.QAction(MainWindow)
        self.actionTriangle.setObjectName(_fromUtf8("actionTriangle"))
        self.actionEllipse = QtGui.QAction(MainWindow)
        self.actionEllipse.setObjectName(_fromUtf8("actionEllipse"))
        self.actionRemove_All = QtGui.QAction(MainWindow)
        self.actionRemove_All.setObjectName(_fromUtf8("actionRemove_All"))
        self.actionArrow_3 = QtGui.QAction(MainWindow)
        self.actionArrow_3.setObjectName(_fromUtf8("actionArrow_3"))
        self.actionArrow_4 = QtGui.QAction(MainWindow)
        self.actionArrow_4.setObjectName(_fromUtf8("actionArrow_4"))
        self.actionArrow_5 = QtGui.QAction(MainWindow)
        self.actionArrow_5.setObjectName(_fromUtf8("actionArrow_5"))
        self.actionArrow_6 = QtGui.QAction(MainWindow)
        self.actionArrow_6.setObjectName(_fromUtf8("actionArrow_6"))
        self.actionRemove_All_2 = QtGui.QAction(MainWindow)
        self.actionRemove_All_2.setObjectName(_fromUtf8("actionRemove_All_2"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave_as = QtGui.QAction(MainWindow)
        self.actionSave_as.setObjectName(_fromUtf8("actionSave_as"))
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.action1_2 = QtGui.QAction(MainWindow)
        self.action1_2.setObjectName(_fromUtf8("action1_2"))
        self.action2_2 = QtGui.QAction(MainWindow)
        self.action2_2.setObjectName(_fromUtf8("action2_2"))
        self.action3_2 = QtGui.QAction(MainWindow)
        self.action3_2.setObjectName(_fromUtf8("action3_2"))
        self.action4_2 = QtGui.QAction(MainWindow)
        self.action4_2.setObjectName(_fromUtf8("action4_2"))
        self.action5_2 = QtGui.QAction(MainWindow)
        self.action5_2.setObjectName(_fromUtf8("action5_2"))
        self.action6_2 = QtGui.QAction(MainWindow)
        self.action6_2.setObjectName(_fromUtf8("action6_2"))
        self.action7_2 = QtGui.QAction(MainWindow)
        self.action7_2.setObjectName(_fromUtf8("action7_2"))
        self.action8_2 = QtGui.QAction(MainWindow)
        self.action8_2.setObjectName(_fromUtf8("action8_2"))
        self.actionBG_Fill = QtGui.QAction(MainWindow)
        self.actionBG_Fill.setObjectName(_fromUtf8("actionBG_Fill"))
        self.actionMax_Min = QtGui.QAction(MainWindow)
        self.actionMax_Min.setObjectName(_fromUtf8("actionMax_Min"))
        self.menuMenu.addAction(self.actionFile)
        self.menuMenu.addAction(self.actionSave)
        self.menuMenu.addAction(self.actionSave_as)
        self.menuMenu.addAction(self.actionClose)
        self.menuNumber_of_Graph_Windows.addAction(self.action1_2)
        self.menuNumber_of_Graph_Windows.addAction(self.action2_2)
        self.menuNumber_of_Graph_Windows.addAction(self.action3_2)
        self.menuNumber_of_Graph_Windows.addAction(self.action4_2)
        self.menuNumber_of_Graph_Windows.addAction(self.action5_2)
        self.menuNumber_of_Graph_Windows.addAction(self.action6_2)
        self.menuNumber_of_Graph_Windows.addAction(self.action7_2)
        self.menuNumber_of_Graph_Windows.addAction(self.action8_2)
        self.menuLayout.addAction(self.menuNumber_of_Graph_Windows.menuAction())
        self.menuScroll.addAction(self.actionStart)
        self.menuScroll.addAction(self.actionPause)
        self.menuScroll.addAction(self.actionResume)
        self.menuScroll.addAction(self.actionStop)
        self.menuScroll.addSeparator()
        self.menuScroll.addAction(self.actionSet_Scroll_Options)
        self.menuInsert_2.addAction(self.actionLine)
        self.menuInsert_2.addAction(self.actionRectangle)
        self.menuInsert_2.addAction(self.actionW)
        self.menuInsert_2.addAction(self.actionM)
        self.menuInsert_2.addAction(self.actionTriangle)
        self.menuInsert_2.addAction(self.actionEllipse)
        self.menuROI.addAction(self.menuInsert_2.menuAction())
        self.menuROI.addAction(self.actionRemove_All)
        self.menuInsert.addAction(self.actionArrow_1)
        self.menuInsert.addAction(self.actionArrow_2)
        self.menuInsert.addAction(self.actionArrow_3)
        self.menuInsert.addAction(self.actionArrow_4)
        self.menuInsert.addAction(self.actionArrow_5)
        self.menuInsert.addAction(self.actionArrow_6)
        self.menuArrow.addAction(self.menuInsert.menuAction())
        self.menuArrow.addAction(self.actionRemove_All_2)
        self.menuBG_Fill.addAction(self.actionBG_Fill)
        self.menuData.addAction(self.actionMax_Min)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuLayout.menuAction())
        self.menubar.addAction(self.menuScroll.menuAction())
        self.menubar.addAction(self.menuROI.menuAction())
        self.menubar.addAction(self.menuArrow.menuAction())
        self.menubar.addAction(self.menuBG_Fill.menuAction())
        self.menubar.addAction(self.menuData.menuAction())
        self.toolBar.addAction(self.actionFile)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionSave_as)
        self.toolBar.addAction(self.actionClose)
        self.toolBar_2.addAction(self.action1_2)
        self.toolBar_2.addAction(self.action2_2)
        self.toolBar_2.addAction(self.action3_2)
        self.toolBar_2.addAction(self.action4_2)
        self.toolBar_2.addAction(self.action5_2)
        self.toolBar_2.addAction(self.action6_2)
        self.toolBar_2.addAction(self.action7_2)
        self.toolBar_2.addAction(self.action8_2)
        self.toolBar_3.addAction(self.actionStart)
        self.toolBar_3.addAction(self.actionPause)
        self.toolBar_3.addAction(self.actionResume)
        self.toolBar_3.addAction(self.actionStop)
        self.toolBar_3.addAction(self.actionSet_Scroll_Options)
        self.toolBar_4.addAction(self.actionLine)
        self.toolBar_4.addAction(self.actionRectangle)
        self.toolBar_4.addAction(self.actionW)
        self.toolBar_4.addAction(self.actionM)
        self.toolBar_4.addAction(self.actionTriangle)
        self.toolBar_4.addAction(self.actionEllipse)
        self.toolBar_4.addAction(self.actionRemove_All)

        """
        Graph Layout 액션에 함수 연결
        """
        self.action1_2.triggered.connect(lambda: self.graphWindow(1))
        self.action2_2.triggered.connect(lambda: self.graphWindow(2))
        self.action3_2.triggered.connect(lambda: self.graphWindow(3))
        self.action4_2.triggered.connect(lambda: self.graphWindow(4))
        self.action5_2.triggered.connect(lambda: self.graphWindow(5))
        self.action6_2.triggered.connect(lambda: self.graphWindow(6))
        self.action7_2.triggered.connect(lambda: self.graphWindow(7))
        self.action8_2.triggered.connect(lambda: self.graphWindow(8))

        """
        self.plotwidget_lst = 그래프를 위에서부터 넣은 리스트
        """
        self.plotwidget_lst = [self.graphicsView, self.graphicsView_2, self.graphicsView_3, self.graphicsView_4, self.graphicsView_5, self.graphicsView_6, self.graphicsView_7, self.graphicsView_8]
        self.plotwidget_lst.reverse()

        """
        File 관련 액션에 함수 연결
        """
        self.actionFile.triggered.connect(self.open)
        self.actionSave.triggered.connect(self.save)
        self.actionSave_as.triggered.connect(self.save_as)
        self.actionClose.triggered.connect(self.close)

        """
        화살표 액션 연결 코드
        """
        self.actionArrow_1.triggered.connect(lambda: self.insertArrow(1))
        self.actionArrow_2.triggered.connect(lambda: self.insertArrow(2))
        self.actionArrow_3.triggered.connect(lambda: self.insertArrow(3))
        self.actionArrow_4.triggered.connect(lambda: self.insertArrow(4))
        self.actionArrow_5.triggered.connect(lambda: self.insertArrow(5))
        self.actionArrow_6.triggered.connect(lambda: self.insertArrow(6))
        self.actionRemove_All_2.triggered.connect(self.removeArrowAll)

        #Scroll function connect
        self.actionStart.triggered.connect(self.startScroll)
        self.actionPause.triggered.connect(self.pauseScroll)
        self.actionResume.triggered.connect(self.resumeScroll)
        self.actionStop.triggered.connect(self.stopScroll)
        self.actionSet_Scroll_Options.triggered.connect(self.optionScroll)

        #ROI function Connect
        self.actionLine.triggered.connect(lambda: self.setROI(0))
        self.actionRectangle.triggered.connect(lambda: self.setROI(1))
        self.actionW.triggered.connect(lambda: self.setROI(2))
        self.actionM.triggered.connect(lambda: self.setROI(3))
        self.actionTriangle.triggered.connect(lambda: self.setROI(4))
        self.actionEllipse.triggered.connect(lambda: self.setROI(5))
        self.actionRemove_All.triggered.connect(self.removeROIAll)

        """
        배경 칠하기 기능 관련 모음
        """
        self.actionBG_Fill.triggered.connect(self.bg_fill)
        self.bg_rect_lst = []

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.restore(MainWindow)

        """
        Max Min 기능 연결
        """
        self.actionMax_Min.triggered.connect(self.data_stat)

        """
        control panel의 tree widget에 mainwindow를 넘겨줌
        """
        self.treeWidget.setMainWindow(self)
        self.treeWidget_2.setMainWindow(self)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMenu.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuLayout.setTitle(QtGui.QApplication.translate("MainWindow", "Layout", None, QtGui.QApplication.UnicodeUTF8))
        self.menuNumber_of_Graph_Windows.setTitle(QtGui.QApplication.translate("MainWindow", "Number of Graph Windows", None, QtGui.QApplication.UnicodeUTF8))
        self.menuScroll.setTitle(QtGui.QApplication.translate("MainWindow", "Scroll", None, QtGui.QApplication.UnicodeUTF8))
        self.menuROI.setTitle(QtGui.QApplication.translate("MainWindow", "ROI", None, QtGui.QApplication.UnicodeUTF8))
        self.menuInsert_2.setTitle(QtGui.QApplication.translate("MainWindow", "Insert", None, QtGui.QApplication.UnicodeUTF8))
        self.menuArrow.setTitle(QtGui.QApplication.translate("MainWindow", "Arrow", None, QtGui.QApplication.UnicodeUTF8))
        self.menuInsert.setTitle(QtGui.QApplication.translate("MainWindow", "Insert", None, QtGui.QApplication.UnicodeUTF8))
        self.menuBG_Fill.setTitle(QtGui.QApplication.translate("MainWindow", "BG Fill", None, QtGui.QApplication.UnicodeUTF8))
        self.menuData.setTitle(QtGui.QApplication.translate("MainWindow", "Data", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFile.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.action12.setText(QtGui.QApplication.translate("MainWindow", "12", None, QtGui.QApplication.UnicodeUTF8))
        self.action1.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.action2.setText(QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.action3.setText(QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.action4.setText(QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.action5.setText(QtGui.QApplication.translate("MainWindow", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.action6.setText(QtGui.QApplication.translate("MainWindow", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.action7.setText(QtGui.QApplication.translate("MainWindow", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.action8.setText(QtGui.QApplication.translate("MainWindow", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStart.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPause.setText(QtGui.QApplication.translate("MainWindow", "Pause", None, QtGui.QApplication.UnicodeUTF8))
        self.actionResume.setText(QtGui.QApplication.translate("MainWindow", "Resume", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStop.setText(QtGui.QApplication.translate("MainWindow", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSet_Scroll_Options.setText(QtGui.QApplication.translate("MainWindow", "Set Scroll Options", None, QtGui.QApplication.UnicodeUTF8))
        self.actionArrow_1.setText(QtGui.QApplication.translate("MainWindow", "Arrow 1", None, QtGui.QApplication.UnicodeUTF8))
        self.actionArrow_2.setText(QtGui.QApplication.translate("MainWindow", "Arrow 2", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLine.setText(QtGui.QApplication.translate("MainWindow", "Line", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRectangle.setText(QtGui.QApplication.translate("MainWindow", "Rectangle", None, QtGui.QApplication.UnicodeUTF8))
        self.actionW.setText(QtGui.QApplication.translate("MainWindow", "W", None, QtGui.QApplication.UnicodeUTF8))
        self.actionM.setText(QtGui.QApplication.translate("MainWindow", "M", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTriangle.setText(QtGui.QApplication.translate("MainWindow", "Triangle", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEllipse.setText(QtGui.QApplication.translate("MainWindow", "Ellipse", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemove_All.setText(QtGui.QApplication.translate("MainWindow", "Remove All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionArrow_3.setText(QtGui.QApplication.translate("MainWindow", "Arrow 3", None, QtGui.QApplication.UnicodeUTF8))
        self.actionArrow_4.setText(QtGui.QApplication.translate("MainWindow", "Arrow 4", None, QtGui.QApplication.UnicodeUTF8))
        self.actionArrow_5.setText(QtGui.QApplication.translate("MainWindow", "Arrow 5", None, QtGui.QApplication.UnicodeUTF8))
        self.actionArrow_6.setText(QtGui.QApplication.translate("MainWindow", "Arrow 6", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemove_All_2.setText(QtGui.QApplication.translate("MainWindow", "Remove All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_as.setText(QtGui.QApplication.translate("MainWindow", "Save as", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.action1_2.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.action2_2.setText(QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.action3_2.setText(QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.action4_2.setText(QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.action5_2.setText(QtGui.QApplication.translate("MainWindow", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.action6_2.setText(QtGui.QApplication.translate("MainWindow", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.action7_2.setText(QtGui.QApplication.translate("MainWindow", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.action8_2.setText(QtGui.QApplication.translate("MainWindow", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBG_Fill.setText(QtGui.QApplication.translate("MainWindow", "BG_Fill", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMax_Min.setText(QtGui.QApplication.translate("MainWindow", "Max_Min", None, QtGui.QApplication.UnicodeUTF8))


    def setSize(self, MainWindow):          # 저장된 설정 파일이 없을 때 최초로 ui 크기를 설정해 주는 함수
        width = MainWindow.width()
        self.splitter_3.setSizes([width/4, 3*width/4])
        self.graphicsView_8.hide()
        self.graphicsView_7.hide()
        self.graphicsView_6.hide()
        self.graphicsView_5.hide()
        self.graphicsView_4.hide()
        self.graphicsView_3.hide()
        self.graphicsView_2.hide()

    def graphWindow(self, num):             # 인자로 받는 num의 수만큼 그래프를 표시해주고 크기도 균등하게 나눔.
        self.num = num
        idx = 0
        width = self.splitter_2.height()/num
        lst = []

        for graph in reversed(self.plotwidget_lst):
            if num > idx:
                graph.show()
                lst.append(width)
            else:
                graph.hide()
                lst.append(0)
            idx += 1

        lst.reverse()
        self.splitter_2.setSizes(lst)
    
    #특정한 파일이 열려있는지 정보를 저장
    is_something_open = False

    def open(self):                         # 파일을 여는 함수. 확장자가 .csv이면 최초로 여는 것이고 .st이면 저장된 세팅을 불러와서 연다. 

        self.fname = ""
        fname = QtGui.QFileDialog.getOpenFileName(None, 'Open file', '~/') 
        name = fname.split("/") 
        
        if name[len(name)-1][-4:] == '.csv':

            if(self.is_something_open == True):
                self.close()
                self.is_something_open = False
                
            self.file_name = name[len(name)-1]
            rd = pd.read_csv(str(fname), index_col=[0], header=None, names=['dt', 'value'])
            rd2 = pd.read_csv(str(fname), header=None, names=['dt', ''])

            self.times = []
            self.lst = [] 

            """
            시간 정보를 받아서 timestamp 형태로 변환
            """
            for dt in rd2.dt:
                try:
                    t = time.strptime(dt, '%Y-%m-%d %H:%M:%S.%f')
                    stamp = time.mktime(t) * 1000 + t.microsecond/1000
                except:
                    stamp = time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M:%S')) * 1000

                self.times += [stamp]

            """
            depth 정보를 리스트에 저장함.
            """
            for val in rd.value: 
                self.lst += [val] 
            
            """
            parameter를 초기화하고 widget에 추가해 줌.
            """
            self.arrowParameter = ArrowParameter(name='Arrow')
            self.roiParameter = ROIParameter(name='ROI')
            self.parameter_1 = Parameter.create(name='Arrow', type='group', children=[self.roiParameter])
            self.treeWidget.setParameters(self.parameter_1, showTop=False)
            self.parameter = Parameter.create(name='Arrow', type='group', children=[self.arrowParameter])
            self.treeWidget_2.setParameters(self.parameter, showTop=False)

            self.graph = CustomGraph(self.lst, self.plotwidget_lst, self.times)

            #ROI Controller
            self.roic = ROIController(self)
            self.roi_setting_lst = []

            #화살표 리스트 초기화
            self.arrow_lst = []
            self.arrow_setting_lst = []
            
            #파일이 열려있다는 것을 알려줌
            self.is_something_open = True

        elif name[len(name)-1].split(".")[1] == "st":

            if(self.is_something_open == True):
                self.close()
                self.is_something_open = False

            self.fname = fname
            f = open(name[len(name)-1], 'r')
            settings = pickle.load(f)
            f.close()
        
            self.file_name = (settings['file_name'])

            #Layout 설정 복구
            self.splitter_3.setSizes(settings['main'])
            self.splitter.setSizes(settings['control'])
            self.graphWindow(settings['graph_num'])
            self.splitter_2.setSizes(settings['graph'])

            #graph_file = './' + settings['file_name']
            rd = pd.read_csv(str(settings['file_name']), index_col=[0], header=None, names=['dt', 'value'])
            rd2 = pd.read_csv(str(settings['file_name']), header=None, names=['dt', ''])

            self.times = []
            self.lst = [] 

            # csv 파일 파싱
            for dt in rd2.dt:
                try:
                    t = time.strptime(dt, '%Y-%m-%d %H:%M:%S.%f')
                    stamp = time.mktime(t) * 1000 + t.microsecond/1000
                except:
                    stamp = time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M:%S')) * 1000

                self.times += [stamp]

            for val in rd.value: 
                self.lst += [val] 
                  
            #화살표 리스트 초기화
            self.arrow_lst = []
            self.arrow_setting_lst = []
                        
            self.arrowParameter = ArrowParameter(name='Arrow')
            self.parameter = Parameter.create(name='Arrow', type='group', children=[self.arrowParameter])
            self.treeWidget_2.setParameters(self.parameter, showTop=False)
            self.roiParameter = ROIParameter(name='ROI')
            self.parameter_1 = Parameter.create(name='Arrow', type='group', children=[self.roiParameter])
            self.treeWidget.setParameters(self.parameter_1, showTop=False)
            self.parameter = Parameter.create(name='Arrow', type='group', children=[self.arrowParameter])
            self.treeWidget_2.setParameters(self.parameter, showTop=False)

            self.graph = CustomGraph(self.lst, self.plotwidget_lst, self.times)
            self.graph.restoreRegion(settings['region_width'])

            """
            화살표 복구
            """
            for arrow in settings['arrow']:
                x = arrow['x']
                y = arrow['y']
                num = arrow['num']
                arrow_type = arrow['type']
                self.arrowRestore(x, y, num, arrow_type)
    
            #ROI Controller
            self.roic = ROIController(self)
            self.roi_setting_lst = []

            # ROI Restore
            for roi in settings['roi']:
                if roi == None:
                    continue
                coor = roi['coor']
                num = roi['num']
                shape = roi['shape']
                self.restoreROI(coor, num, shape)
            
            #파일이 열려있다는 것을 알려줌
            self.is_something_open = True

    def save_setting(self):
        # 화면 Layout을 저장한다. 표시되는 그래프의 수 및 각 layout의 크기를 저장.
        main_setting = self.splitter_3.sizes()
        control_setting = self.splitter.sizes()
        graph_setting = self.splitter_2.sizes()

        graph_num = 0
        for graph in graph_setting:
            if graph != 0:
                graph_num += 1
        settings = {'main': main_setting, 'control': control_setting, 'graph': graph_setting, 'graph_num': graph_num}
        f = open('setting', 'w+')
        pickle.dump(settings, f)
        f.close()
        
    def save(self):                     # 저장해야 될 정보를 저장하는 함수. pickle을 이용해서 저장한다.
        if self.fname is not "":
            pass            
        else:
            self.fname = QtGui.QFileDialog.getSaveFileName(None, 'Save file', '~/') + ".st"

        name = self.fname.split("/")
        
        region_width_lst = []           # 파일 이름 및 Region 저장
        for region in self.graph.region_lst:
            region_width_lst.append(region.getRegion())
        
        main_setting = self.splitter_3.sizes()
        control_setting = self.splitter.sizes()
        graph_setting = self.splitter_2.sizes()

        graph_num = 0
        for graph in graph_setting:
            if graph != 0:
                graph_num += 1

        settings = {'file_name': self.file_name, 'region_width': region_width_lst, 'main': main_setting, 'control': control_setting, 'graph': graph_setting, 'graph_num': graph_num, 'arrow': self.arrow_setting_lst, 'roi': self.roi_setting_lst}

        f = open(name[len(name)-1], 'w+')
        pickle.dump(settings, f)
        f.close()
        

    """
    최초로 save할 때와 같은 함수 내용을 사용한다.
    """
    def save_as(self):
        self.fname = QtGui.QFileDialog.getSaveFileName(None, 'Save file As', '~/') + ".st"
        name = self.fname.split("/")
        
        region_width_lst = []           # 파일 이름 및 Region 저장
        for region in self.graph.region_lst:
            region_width_lst.append(region.getRegion())
        
        main_setting = self.splitter_3.sizes()
        control_setting = self.splitter.sizes()
        graph_setting = self.splitter_2.sizes()

        graph_num = 0
        for graph in graph_setting:
            if graph != 0:
                graph_num += 1

        settings = {'file_name': self.file_name, 'region_width': region_width_lst, 'main': main_setting, 'control': control_setting, 'graph': graph_setting, 'graph_num': graph_num, 'arrow': self.arrow_setting_lst, 'roi': self.roi_setting_lst}

        f = open(name[len(name)-1], 'w+')
        pickle.dump(settings, f)
        f.close()
        
    """
    저장 파일의 이름을 초기화하고 widget에서 plot을 지우고 ROI와 Arrow Parameter를 지운다.
    """
    def close(self):
        self.fname = ""

        for widget in self.plotwidget_lst:
            widget.clear()

        self.roic.clear()

        self.arrowParameter.remove()
        self.roiParameter.remove()

        self.is_something_open = False

    #최초에 프로그램을 열 때 호출되는 함수로, 저장된 layout설정 파일이 있으면 파일을 열어서 설정을 복구한다.
    def restore(self, MainWindow):
        try:
            f = open('setting', 'r')
            settings = pickle.load(f)
            self.splitter_3.setSizes(settings['main'])
            self.splitter.setSizes(settings['control'])
            self.graphWindow(settings['graph_num'])
            self.splitter_2.setSizes(settings['graph'])
        
        except IOError:
            self.setSize(MainWindow)
            self.graphWindow(1)

    """
    화살표 삽입 함수. 화살표 종류를 int 인자로 받아서 타입에 맞춰 적절한 화살표를 삽입한다.
    가장 아래쪽에 있는 그래프의 가운데에 삽입하도록 되어있다. 각 graph widget에 삽입한 화살표를 리스트로 만들고
    그 리스트를 다시 self.arrow_lst라는 리스트에 추가한다.
    마지막으로 이 화살표에 해당하는 parameter를 추가한다.
    """
    def insertArrow(self, arrow_type):
        arrow_lst = []
        for widget in self.plotwidget_lst:
            if arrow_type == 1:
                arrow = pg.ArrowItem(angle=-120, tipAngle=30, baseAngle=20, headLen=20, tailLen=20, tailWidth=10, brush='b')
            elif arrow_type == 2:
                arrow = pg.ArrowItem(angle=-90, tipAngle=30, baseAngle=20, headLen=20, tailLen=20, tailWidth=10, brush='b')
            elif arrow_type == 3:
                arrow = pg.ArrowItem(angle=-60, tipAngle=30, baseAngle=20, headLen=20, tailLen=20, tailWidth=10, brush='b')
            elif arrow_type == 4:
                arrow = pg.ArrowItem(angle=-120, tipAngle=30, baseAngle=20, headLen=20, tailLen=20, tailWidth=10, brush='r')
            elif arrow_type == 5:
                arrow = pg.ArrowItem(angle=-90, tipAngle=30, baseAngle=20, headLen=20, tailLen=20, tailWidth=10, brush='r')
            else:
                arrow = pg.ArrowItem(angle=-60, tipAngle=30, baseAngle=20, headLen=20, tailLen=20, tailWidth=10, brush='r')

            x1, x2 = self.plotwidget_lst[7-self.num+1].getViewBox().viewRange()[0]
            x_pos = (x2-x1)/2 + x1
            i = bisect_right(self.times, x_pos) 
            arrow.setPos(self.times[i], self.lst[i])
            widget.addItem(arrow)
            arrow_lst.append(arrow)
        
        self.arrow_lst.append(arrow_lst)
        num = self.arrowParameter.addArrow(datetime.fromtimestamp(x_pos/1000).strftime('%y-%m-%d %H:%M:%S'), self.lst[i], arrow_type)
        self.arrow_setting_lst.append({'x': self.times[i], 'y': self.lst[i], 'num': num, 'type': arrow_type})

    """
    저장된 화살표를 복구하기 위해 사용하는 함수
    """
    def arrowRestore(self, x, y, num, arrow_type):
        arrow_lst = []
        for widget in self.plotwidget_lst:
            if arrow_type == 1:
                arrow = pg.ArrowItem(angle=-120, tipAngle=30, baseAngle=20, headLen=20, tailLen=20, tailWidth=10, brush='b')
            elif arrow_type == 2:
                arrow = pg.ArrowItem(angle=-90, tipAngle=30, baseAngle=20, headLen=20, tailLen=20, tailWidth=10, brush='b')
            elif arrow_type == 3:
                arrow = pg.ArrowItem(angle=-60, tipAngle=30, baseAngle=20, headLen=20, tailLen=20, tailWidth=10, brush='b')
            elif arrow_type == 4:
                arrow = pg.ArrowItem(angle=-120, tipAngle=30, baseAngle=20, headLen=20, tailLen=20, tailWidth=10, brush='r')
            elif arrow_type == 5:
                arrow = pg.ArrowItem(angle=-90, tipAngle=30, baseAngle=20, headLen=20, tailLen=20, tailWidth=10, brush='r')
            else:
                arrow = pg.ArrowItem(angle=-60, tipAngle=30, baseAngle=20, headLen=20, tailLen=20, tailWidth=10, brush='r')

            arrow.setPos(x, y)
            widget.addItem(arrow)
            arrow_lst.append(arrow)

        self.arrow_lst.append(arrow_lst)
        self.arrowParameter.restoreArrow(datetime.fromtimestamp(x/1000).strftime('%y-%m-%d %H:%M:%S'), y, num, arrow_type)
        self.arrow_setting_lst.append({'x': x, 'y': y, 'num': num, 'type': arrow_type})


    """
    item으로 받은 화살표를 제거할 때에 사용된다.
    그래프 상에서 제거할 뿐만 아니라 parameter에서 제거할 수 있도록
    parameter의 제거 함수를 호출한다.
    """
    def removeArrow(self, item):
        arrow_num = int(item.text(0).split("Arrow")[1])
        
        i = 0
        for arrow_setting in self.arrow_setting_lst:
            if arrow_setting['num'] == arrow_num:
                d = arrow_setting
                break
            i += 1

        for (arrow, widget) in zip(self.arrow_lst[i], self.plotwidget_lst):
            widget.removeItem(arrow)
        
        
        self.arrow_setting_lst.remove(d)
        self.arrowParameter.removeArrow(item.text(0))
            
    """
    모든 화살표를 제거한다. parameter도 함께 제거함.
    """
    def removeArrowAll(self):
        for arrow_lst in self.arrow_lst:
            for (arrow, widget) in zip(arrow_lst, self.plotwidget_lst):
                widget.removeItem(arrow)

        self.arrow_lst = []
        self.arrow_setting_lst = []
        self.arrowParameter.removeArrowAll()
    
    timer = 0

    #스크롤이 현재 진행되고 있는지 저장
    scroll_active = False
    #이벤트 함수 호출을 위한 타이머 오브젝트 저장공간
    timer = 0
    #1초당 움직이는 범위
    velocity = 10
    #스크롤 할 그래프의 레벨
    scroll_level = 1
    #스크롤 하면서 움직일 애로우 오브젝트 저장공간
    curve_arrow = 0

    def scrollEvent(self):
        """
        스크롤 시 타이머에 의해 호출되어 그래프를 스크롤하는 함수
        """
        cont = self.graph.scroll(self.plotwidget_lst[8-self.scroll_level], self.scroll_level, self.velocity, self.curve_arrow)
        
        #자동스크롤 시 화면 범위를 넘어가면 콘솔에 메세지를 출력하고 스크롤이 중단됨
        if cont == False:
            print('Out of Bonud!')
            self.pauseScroll()
    
    def startScroll(self):    
        """

        """
        if(self.timer!=0):
            return
        
        cur_viewrange = self.plotwidget_lst[8-self.scroll_level].getViewBox().viewRange()[0]
        cur_region = self.graph.region_lst[8-self.scroll_level].getRegion()
        #cur_pos = (((cur_region[0] + cur_region[1])/2) - cur_viewrange[0]) / (cur_viewrange[1] - cur_viewrange[0])
        cur_region_mid = (cur_region[0] + cur_region[1])/2
        cur_index = bisect_left(self.graph.times, cur_region_mid)
        #print cur_pos
        self.curve_arrow = pg.CurveArrow(self.plotwidget_lst[8-self.scroll_level].getPlotItem().listDataItems()[0], index=cur_index)
        #self.curve_arrow = pg.CurveArrow(self.plotwidget_lst[8-self.scroll_level].getPlotItem(), pos=0.5)
        self.plotwidget_lst[8-self.scroll_level].addItem(self.curve_arrow)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.scrollEvent)
        self.scroll_active = True
        self.timer.start(250)

    def pauseScroll(self):
        try:
            if(self.scroll_active != True):
                return
            self.scroll_active = False
            self.timer.stop()

        except:
            print('Error!')

    def resumeScroll(self):
        try:
            if(self.scroll_active != False):
                return
            self.timer.start(250)
            self.scroll_active = True
        except:
            print('Error!')

    def stopScroll(self):
        try:
            del self.timer
            self.timer = 0

            self.plotwidget_lst[8-self.scroll_level].removeItem(self.curve_arrow)
            del self.curve_arrow
            self.curve_arrow = 0
            self.cur_pos = 0

            self.scroll_active = False
        except:
            print('Error!')

    def optionScroll(self):
        self.w = ScrollPopup(self)
        #self.w.setGeometry(QtCore.QRect(100, 100, 400, 400))
        #self.w.show()

    def parameterScroll(self, param_name):
        if param_name.contains('Arrow'):
            arrow = True
            num = param_name.split('Arrow')[1]
        else:
            arrow = False
            num = param_name.split('ROI')[1]

        if arrow:
            for arrow_setting in self.arrow_setting_lst:
                if arrow_setting['num'] == int(num):
                    self.graph.parameterScroll(arrow_setting['x'], self.plotwidget_lst)
        else:
            for roi_setting in self.roi_setting_lst:
                if roi_setting['num'] == int(num):
                    ((x1, _), (x2, _)) = roi_setting['coor']
                    self.graph.parameterScroll((x1 + x2) / 2, self.plotwidget_lst)

    """
    지정된 영역에 대해 배경색을 변경하도록 한다.
    시작 일시와 종료 일시 모두 현 그래프의 시작점으로 맞춰준다.
    """
    def bg_fill(self):
        self.bg = BG_Popup.BGFill_Dialog(self.times[0])
        value = self.bg.activate()

        if len(self.bg_rect_lst) != 0:
            for (rect, widget) in zip(self.bg_rect_lst, self.plotwidget_lst):
                widget.removeItem(rect)
            self.bg_rect_lst = []

        start = value['start']
        end = value['end']
    
        start_stamp = time.mktime(datetime(start['year'], start['month'], start['day'], start['time'].hour(), start['time'].minute(), start['time'].second()).timetuple()) * 1000
        end_stamp = time.mktime(datetime(end['year'], end['month'], end['day'], end['time'].hour(), end['time'].minute(), end['time'].second()).timetuple()) * 1000
        
        for widget in self.plotwidget_lst:
            rect = pg.QtGui.QGraphicsRectItem(start_stamp, -10000, end_stamp-start_stamp, 20000)
            rect.setBrush(pg.mkBrush('#C9BB89'))
            rect.setZValue(-1000)
            widget.addItem(rect)
            self.bg_rect_lst.append(rect)

    """
    Max와 Min을 보여주는 기능. 그래프 별로 보이는 영역의 범위를 얻어온 뒤
    그 안에 해당하는 y축 값들에서 최대 최소인 값을 찾아낸 뒤 팝업에 넘겨준다.
    """
    def data_stat(self):
        max_lst = []
        min_lst = []
        self.plotwidget_lst.reverse()
        for widget in self.plotwidget_lst[0:self.num]:
            x1, x2 = widget.getViewBox().viewRange()[0]
            x_start = bisect_right(self.times, x1)
            x_end = bisect_left(self.times, x2)

            if x_start < x_end:
                max_lst.append(max(self.lst[x_start:x_end]))
                min_lst.append(min(self.lst[x_start:x_end]))
            else:
                max_lst.append('empty')
                min_lst.append('empty')
        
        self.plotwidget_lst.reverse()
        values = {'max': max_lst, 'min': min_lst}
        ds = Data_Popup.DataStat_Dialog(values)
    
    # ROI
    def dragev(self, ev, i, shape):
        '''ROI를 삽입할 때의 마우스 드래그 이벤트 관리 함수이다.
        마우스로 드래그한 영역의 좌표를 계산하여, 이를 바탕으로 
        ROI를 삽입한다'''

        ev.accept()
        vb = self.plotwidget_lst[i].getViewBox()
        pos = ev.pos()
        if self.roi_loc == 1 and ev.button() == QtCore.Qt.LeftButton:                                                                      
            if ev.isFinish():                                                                                                                
                vb.rbScaleBox.hide()
                # set region
                _, _, xax, yax = vb.rect().getCoords()
                x1, x2 = self.plotwidget_lst[i].getViewBox().viewRange()[0]
                y1, y2 = self.plotwidget_lst[i].getViewBox().viewRange()[1]
                p1, p2 = ev.buttonDownPos(ev.button()), pos
                xlen, ylen = x2-x1, y2-y1
                fx1 = x1 + xlen*p1.x()/xax
                fy1 = y1 + ylen*(yax-p1.y())/yax
                fx2 = x1 + xlen*p2.x()/xax
                fy2 = y1 + ylen*(yax-p2.y())/yax
                # make ROI
                self.roic.setROI(shape, ((fx1, fy1), (fx2, fy2)))
                self.roi_loc = 0
                num = self.roiParameter.addROI(datetime.fromtimestamp((fx1+fx2)/2000).strftime('%y-%m-%d %H:%M:%S'), shape)
                self.roi_setting_lst.append({'coor': ((fx1, fy1), (fx2, fy2)), 'num': num, 'shape': shape})
            else:                                                                                                               
                vb.updateScaleBox(ev.buttonDownPos(), ev.pos())
        else:
            pg.ViewBox.mouseDragEvent(vb, ev)

    def setROI(self, shape):
        '''드래그로 범위 지정을 하기위해 위젯 뷰의 마우스
        이벤트를 조작한다.'''
        
        self.roi_loc = 1
        self.plotwidget_lst[0].getViewBox().mouseDragEvent = (lambda ev: self.dragev(ev, 0, shape))
        self.plotwidget_lst[1].getViewBox().mouseDragEvent = (lambda ev: self.dragev(ev, 1, shape))
        self.plotwidget_lst[2].getViewBox().mouseDragEvent = (lambda ev: self.dragev(ev, 2, shape))
        self.plotwidget_lst[3].getViewBox().mouseDragEvent = (lambda ev: self.dragev(ev, 3, shape))
        self.plotwidget_lst[4].getViewBox().mouseDragEvent = (lambda ev: self.dragev(ev, 4, shape))
        self.plotwidget_lst[5].getViewBox().mouseDragEvent = (lambda ev: self.dragev(ev, 5, shape))
        self.plotwidget_lst[6].getViewBox().mouseDragEvent = (lambda ev: self.dragev(ev, 6, shape))
        self.plotwidget_lst[7].getViewBox().mouseDragEvent = (lambda ev: self.dragev(ev, 7, shape))

    def restoreROI(self, coor, num, shape):
        '''OPEN 시에 ROI를 복구하는 메서드이다'''
        
        (x1, _), (x2, _) = coor
        self.roic.setROI(shape, coor)
        self.roiParameter.restoreROI(datetime.fromtimestamp((x1+x2)/2000).strftime('%y-%m-%d %H:%M:%S'), num, shape)
        self.roi_setting_lst.append({'coor': coor, 'num': num, 'shape': shape})

    def removeROIByObj(self, roi):
        '''ROI 오브젝트를 인자로 받아 해당 ROI를 제거한다'''

        roi_num = 0
        for rois in self.roic.getROIList():
            if rois == None:
                continue
            else:
                found = False
                for aroi in rois:
                    if aroi == roi:
                        found = True
                        break
                if found:
                    break
            roi_num += 1
        for i in xrange(len(self.roi_setting_lst)):
            if self.roi_setting_lst[i] == None:
                continue
            elif self.roi_setting_lst[i]['num'] == roi_num:
                self.roi_setting_lst[i] = None
                self.roic.removeROI(i)
                break
        self.roiParameter.removeROI("ROI"+str(roi_num))

    def removeROIByItem(self, item):
        '''Parameter의 ROI 아이템을 인자로 받아 해당 ROI를 제거하는 메서드'''
        roi_num = int(item.text(0).split("ROI")[1])
        for i in xrange(len(self.roi_setting_lst)):
            if self.roi_setting_lst[i] == None:
                continue
            elif self.roi_setting_lst[i]['num'] == roi_num:
                self.roi_setting_lst[i] = None
                self.roic.removeROI(i)
                break
        self.roiParameter.removeROI(item.text(0))
    
    def popupROI(self):
        ROIPopup(self)

    def removeROIAll(self):
        self.roic.removeAll()
        self.roiParameter.removeROIAll()

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
    def keyPressEvent(self, event):
        #Scroll mapping keys
        if (event.key()==QtCore.Qt.Key_Q):
            self.ui.startScroll()

        elif(event.key()==QtCore.Qt.Key_W):
            self.ui.pauseScroll()

        elif(event.key()==QtCore.Qt.Key_E):
            self.ui.resumeScroll()

        elif(event.key()==QtCore.Qt.Key_R):
            self.ui.stopScroll()
        
        elif(event.key()==QtCore.Qt.Key_Up):
            self.ui.velocity *= 1.25
        
        elif(event.key()==QtCore.Qt.Key_Down):
            self.ui.velocity *= 0.8
        elif(event.key()==QtCore.Qt.Key_Left):
            if(self.ui.scroll_active == False):
                self.ui.graph.scroll(self.ui.plotwidget_lst[8-self.ui.scroll_level], self.ui.scroll_level, -1*self.ui.velocity, self.ui.curve_arrow)
        elif(event.key()==QtCore.Qt.Key_Right):
            if(self.ui.scroll_active == False):
                self.ui.graph.scroll(self.ui.plotwidget_lst[8-self.ui.scroll_level], self.ui.scroll_level, self.ui.velocity, self.ui.curve_arrow)

        # Arrow Mapping Keys
        elif(event.key()==QtCore.Qt.Key_4):
            self.ui.insertArrow(1)
        elif(event.key()==QtCore.Qt.Key_5):
            self.ui.insertArrow(2)
        elif(event.key()==QtCore.Qt.Key_6):
            self.ui.insertArrow(3)
        elif(event.key()==QtCore.Qt.Key_7):
            self.ui.insertArrow(4)
        elif(event.key()==QtCore.Qt.Key_8):
            self.ui.insertArrow(5)
        elif(event.key()==QtCore.Qt.Key_9):
            self.ui.insertArrow(6)
        
    def closeEvent(self, event):
        self.ui.save_setting()


    #def mousePressEvent(self, event):
    #    print 'hi'

    def closeEvent(self, event):
        self.ui.save_setting()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = Window()
    MainWindow.show()
    sys.exit(app.exec_())

