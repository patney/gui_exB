# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\src\ui\raw_ui\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(638, 496)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 601, 421))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.tabWidget = QtWidgets.QTabWidget(self.page_5)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 551, 381))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setIconSize(QtCore.QSize(5, 5))
        self.tabWidget.setObjectName("tabWidget")
        self.MACAddresses = QtWidgets.QWidget()
        self.MACAddresses.setObjectName("MACAddresses")
        self.frame = QtWidgets.QFrame(self.MACAddresses)
        self.frame.setGeometry(QtCore.QRect(400, 20, 101, 80))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(20, 10, 70, 14))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton.sizePolicy().hasHeightForWidth())
        self.radioButton.setSizePolicy(sizePolicy)
        self.radioButton.setMaximumSize(QtCore.QSize(16777215, 14))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 30, 70, 14))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_2.sizePolicy().hasHeightForWidth())
        self.radioButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 50, 70, 14))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_3.sizePolicy().hasHeightForWidth())
        self.radioButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.chec_box_frame = QtWidgets.QGroupBox(self.MACAddresses)
        self.chec_box_frame.setGeometry(QtCore.QRect(250, 60, 131, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chec_box_frame.sizePolicy().hasHeightForWidth())
        self.chec_box_frame.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.chec_box_frame.setFont(font)
        self.chec_box_frame.setObjectName("chec_box_frame")
        self.checkBox = QtWidgets.QCheckBox(self.chec_box_frame)
        self.checkBox.setGeometry(QtCore.QRect(20, 20, 80, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkBox.setFont(font)
        self.checkBox.setAutoExclusive(True)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.chec_box_frame)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 40, 80, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setAutoExclusive(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.chec_box_frame)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 60, 80, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_3.sizePolicy().hasHeightForWidth())
        self.checkBox_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setAutoExclusive(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.RadioExample_2 = QtWidgets.QGroupBox(self.MACAddresses)
        self.RadioExample_2.setGeometry(QtCore.QRect(250, 150, 131, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RadioExample_2.sizePolicy().hasHeightForWidth())
        self.RadioExample_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.RadioExample_2.setFont(font)
        self.RadioExample_2.setObjectName("RadioExample_2")
        self.checkBox_7 = QtWidgets.QCheckBox(self.RadioExample_2)
        self.checkBox_7.setGeometry(QtCore.QRect(20, 20, 70, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_7.sizePolicy().hasHeightForWidth())
        self.checkBox_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkBox_7.setFont(font)
        self.checkBox_7.setAutoExclusive(False)
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self.RadioExample_2)
        self.checkBox_8.setGeometry(QtCore.QRect(20, 40, 70, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_8.sizePolicy().hasHeightForWidth())
        self.checkBox_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkBox_8.setFont(font)
        self.checkBox_8.setAutoExclusive(False)
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(self.RadioExample_2)
        self.checkBox_9.setGeometry(QtCore.QRect(20, 60, 70, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_9.sizePolicy().hasHeightForWidth())
        self.checkBox_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkBox_9.setFont(font)
        self.checkBox_9.setAutoExclusive(False)
        self.checkBox_9.setObjectName("checkBox_9")
        self.pushButton = QtWidgets.QPushButton(self.MACAddresses)
        self.pushButton.setGeometry(QtCore.QRect(10, 42, 70, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.input_box = QtWidgets.QLineEdit(self.MACAddresses)
        self.input_box.setGeometry(QtCore.QRect(90, 40, 113, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_box.sizePolicy().hasHeightForWidth())
        self.input_box.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.input_box.setFont(font)
        self.input_box.setObjectName("input_box")
        self.spinBox = QtWidgets.QSpinBox(self.MACAddresses)
        self.spinBox.setGeometry(QtCore.QRect(140, 70, 61, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spinBox.setFont(font)
        self.spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spinBox.setProperty("showGroupSeparator", True)
        self.spinBox.setMaximum(30000)
        self.spinBox.setSingleStep(500)
        self.spinBox.setObjectName("spinBox")
        self.listWidget = QtWidgets.QListWidget(self.MACAddresses)
        self.listWidget.setGeometry(QtCore.QRect(10, 100, 211, 131))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.progressBar = QtWidgets.QProgressBar(self.MACAddresses)
        self.progressBar.setGeometry(QtCore.QRect(10, 260, 261, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.toolBox = QtWidgets.QToolBox(self.MACAddresses)
        self.toolBox.setGeometry(QtCore.QRect(400, 110, 141, 171))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.toolBox.setFont(font)
        self.toolBox.setFrameShape(QtWidgets.QFrame.Panel)
        self.toolBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 139, 121))
        self.page.setObjectName("page")
        self.tool_box_bttn1 = QtWidgets.QPushButton(self.page)
        self.tool_box_bttn1.setGeometry(QtCore.QRect(30, 10, 80, 17))
        self.tool_box_bttn1.setObjectName("tool_box_bttn1")
        self.tool_box_cbox = QtWidgets.QCheckBox(self.page)
        self.tool_box_cbox.setGeometry(QtCore.QRect(30, 33, 70, 14))
        self.tool_box_cbox.setObjectName("tool_box_cbox")
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 139, 121))
        self.page_2.setObjectName("page_2")
        self.tool_box_pg2_bttn_1 = QtWidgets.QPushButton(self.page_2)
        self.tool_box_pg2_bttn_1.setGeometry(QtCore.QRect(30, 10, 70, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tool_box_pg2_bttn_1.sizePolicy().hasHeightForWidth())
        self.tool_box_pg2_bttn_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tool_box_pg2_bttn_1.setFont(font)
        self.tool_box_pg2_bttn_1.setObjectName("tool_box_pg2_bttn_1")
        self.tool_box_pg2_bttn_2 = QtWidgets.QPushButton(self.page_2)
        self.tool_box_pg2_bttn_2.setGeometry(QtCore.QRect(30, 40, 70, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tool_box_pg2_bttn_2.sizePolicy().hasHeightForWidth())
        self.tool_box_pg2_bttn_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tool_box_pg2_bttn_2.setFont(font)
        self.tool_box_pg2_bttn_2.setObjectName("tool_box_pg2_bttn_2")
        self.toolBox.addItem(self.page_2, "")
        self.warning_label = QtWidgets.QLabel(self.MACAddresses)
        self.warning_label.setGeometry(QtCore.QRect(10, 310, 91, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.warning_label.sizePolicy().hasHeightForWidth())
        self.warning_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.warning_label.setFont(font)
        self.warning_label.setStyleSheet("color: rgb(170, 0, 0);")
        self.warning_label.setTextFormat(QtCore.Qt.PlainText)
        self.warning_label.setObjectName("warning_label")
        self.change_label_color_bttn = QtWidgets.QPushButton(self.MACAddresses)
        self.change_label_color_bttn.setGeometry(QtCore.QRect(120, 310, 110, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.change_label_color_bttn.sizePolicy().hasHeightForWidth())
        self.change_label_color_bttn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.change_label_color_bttn.setFont(font)
        self.change_label_color_bttn.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.change_label_color_bttn.setFlat(False)
        self.change_label_color_bttn.setObjectName("change_label_color_bttn")
        self.style_sheet_box = QtWidgets.QLineEdit(self.MACAddresses)
        self.style_sheet_box.setGeometry(QtCore.QRect(240, 310, 261, 20))
        self.style_sheet_box.setObjectName("style_sheet_box")
        self.label = QtWidgets.QLabel(self.MACAddresses)
        self.label.setGeometry(QtCore.QRect(250, 290, 71, 20))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.MACAddresses, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.return_to_tab1_bttn = QtWidgets.QPushButton(self.tab_2)
        self.return_to_tab1_bttn.setGeometry(QtCore.QRect(20, 40, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.return_to_tab1_bttn.setFont(font)
        self.return_to_tab1_bttn.setObjectName("return_to_tab1_bttn")
        self.tabWidget.addTab(self.tab_2, "")
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.listView = QtWidgets.QListView(self.page_6)
        self.listView.setGeometry(QtCore.QRect(10, 20, 256, 192))
        self.listView.setObjectName("listView")
        self.treeView = QtWidgets.QTreeView(self.page_6)
        self.treeView.setGeometry(QtCore.QRect(10, 220, 256, 192))
        self.treeView.setObjectName("treeView")
        self.pushButton_5 = QtWidgets.QPushButton(self.page_6)
        self.pushButton_5.setGeometry(QtCore.QRect(280, 20, 56, 17))
        self.pushButton_5.setObjectName("pushButton_5")
        self.stackedWidget.addWidget(self.page_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 638, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.dockWidget.setFont(font)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton.setText(_translate("MainWindow", "RadioButton"))
        self.radioButton_2.setText(_translate("MainWindow", "RadioButton"))
        self.radioButton_3.setText(_translate("MainWindow", "RadioButton"))
        self.chec_box_frame.setTitle(_translate("MainWindow", "Exclusive Check Boxes"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox1"))
        self.checkBox_2.setText(_translate("MainWindow", "CheckBox2"))
        self.checkBox_3.setText(_translate("MainWindow", "CheckBox3"))
        self.RadioExample_2.setTitle(_translate("MainWindow", "Non Exclusive Check Boxes"))
        self.checkBox_7.setText(_translate("MainWindow", "CheckBox1"))
        self.checkBox_8.setText(_translate("MainWindow", "CheckBox2"))
        self.checkBox_9.setText(_translate("MainWindow", "CheckBox3"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Example Text"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.tool_box_bttn1.setText(_translate("MainWindow", "PushButton"))
        self.tool_box_cbox.setText(_translate("MainWindow", "CheckBox"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Page 1"))
        self.tool_box_pg2_bttn_1.setText(_translate("MainWindow", "Show Popup"))
        self.tool_box_pg2_bttn_2.setText(_translate("MainWindow", "PushButton"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Page 2"))
        self.warning_label.setText(_translate("MainWindow", "This Label is Red"))
        self.change_label_color_bttn.setText(_translate("MainWindow", "Change Label Color"))
        self.label.setText(_translate("MainWindow", "StyleSheet"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MACAddresses), _translate("MainWindow", "Tab1"))
        self.return_to_tab1_bttn.setText(_translate("MainWindow", "Return to Tab1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))