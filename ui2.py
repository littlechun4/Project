# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui2.ui'
#
# Created: Tue Dec  3 16:50:49 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter_2 = QtGui.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.textBrowser = QtGui.QTextBrowser(self.splitter_2)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.splitter = QtGui.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.graphicsView = QtGui.QGraphicsView(self.splitter)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.graphicsView_2 = QtGui.QGraphicsView(self.splitter)
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        self.graphicsView_4 = QtGui.QGraphicsView(self.splitter)
        self.graphicsView_4.setObjectName(_fromUtf8("graphicsView_4"))
        self.graphicsView_3 = QtGui.QGraphicsView(self.splitter)
        self.graphicsView_3.setObjectName(_fromUtf8("graphicsView_3"))
        self.gridLayout.addWidget(self.splitter_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 844, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        self.menuLayout = QtGui.QMenu(self.menubar)
        self.menuLayout.setObjectName(_fromUtf8("menuLayout"))
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
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
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
        self.menuMenu.addAction(self.actionFile)
        self.menuMenu.addAction(self.actionSave)
        self.menuMenu.addAction(self.actionSave_as)
        self.menuMenu.addAction(self.actionClose)
        self.menuLayout.addAction(self.action1)
        self.menuLayout.addAction(self.action2)
        self.menuLayout.addAction(self.action3)
        self.menuLayout.addAction(self.action4)
        self.menuLayout.addAction(self.action5)
        self.menuLayout.addAction(self.action6)
        self.menuLayout.addAction(self.action7)
        self.menuLayout.addAction(self.action8)
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
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuLayout.menuAction())
        self.menubar.addAction(self.menuScroll.menuAction())
        self.menubar.addAction(self.menuROI.menuAction())
        self.menubar.addAction(self.menuArrow.menuAction())
        self.menubar.addAction(self.menuBG_Fill.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMenu.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuLayout.setTitle(QtGui.QApplication.translate("MainWindow", "Layout", None, QtGui.QApplication.UnicodeUTF8))
        self.menuScroll.setTitle(QtGui.QApplication.translate("MainWindow", "Scroll", None, QtGui.QApplication.UnicodeUTF8))
        self.menuROI.setTitle(QtGui.QApplication.translate("MainWindow", "ROI", None, QtGui.QApplication.UnicodeUTF8))
        self.menuInsert_2.setTitle(QtGui.QApplication.translate("MainWindow", "Insert", None, QtGui.QApplication.UnicodeUTF8))
        self.menuArrow.setTitle(QtGui.QApplication.translate("MainWindow", "Arrow", None, QtGui.QApplication.UnicodeUTF8))
        self.menuInsert.setTitle(QtGui.QApplication.translate("MainWindow", "Insert", None, QtGui.QApplication.UnicodeUTF8))
        self.menuBG_Fill.setTitle(QtGui.QApplication.translate("MainWindow", "BG Fill", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
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
        self.actionRemove_All.setText(QtGui.QApplication.translate("MainWindow", "Remove All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionArrow_3.setText(QtGui.QApplication.translate("MainWindow", "Arrow 3", None, QtGui.QApplication.UnicodeUTF8))
        self.actionArrow_4.setText(QtGui.QApplication.translate("MainWindow", "Arrow 4", None, QtGui.QApplication.UnicodeUTF8))
        self.actionArrow_5.setText(QtGui.QApplication.translate("MainWindow", "Arrow 5", None, QtGui.QApplication.UnicodeUTF8))
        self.actionArrow_6.setText(QtGui.QApplication.translate("MainWindow", "Arrow 6", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemove_All_2.setText(QtGui.QApplication.translate("MainWindow", "Remove All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_as.setText(QtGui.QApplication.translate("MainWindow", "Save as", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

