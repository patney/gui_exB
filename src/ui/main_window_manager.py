# coding=utf-8

import sys
# Threads can be used to keep a progress bar active while a function is running.
from multiprocessing.pool import ThreadPool

# Import PyQT5 widgets.
import PyQt5.QtWidgets as Qt
from PyQt5 import QtCore, QtWidgets

# Impoort custom pop-up.
from src.util.pop_message import PopMessage

# Import the main GUI.
from src.ui.main_window import Ui_MainWindow

pool = ThreadPool(processes=4)


class MainOveride(Qt.QMainWindow):
    """
        Overwrite the QtGui.QMainWindow closeEvent method
        so we can ask the user if they are sure to exit.
    """

    def closeEvent(self, event):
        result = Qt.QMessageBox.question(self,
                                            "Confirm Exit",
                                            "<b>Are you sure you want to Exit?",
                                            Qt.QMessageBox.Yes | Qt.QMessageBox.No)
        event.ignore()

        if result == Qt.QMessageBox.Yes:
            Qt.QApplication.closeAllWindows()
            event.accept()

''' R E V I S I O N '''
revision = '1.0'


class MainWindow(Ui_MainWindow, MainOveride):
    # Handle high resolution displays:
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    # The GUI application.
    app = Qt.QApplication(sys.argv)

    # Sets the stype for the GUI
    app.setStyle('Windows')

    pass_color = "color: rgb(0, 170, 0); background-color: rgb(255, 255, 255);"
    fail_color = "color: rgb(170, 0, 0); background-color: rgb(255, 255, 255);"
    default_color = "color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);"

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        #  Pass the parent to PopMessage
        # PopMessage is an example of adding custom GUIs.
        self.user_message = PopMessage(self)

        # Setup the Designer UI.
        self.setupUi(self)

        # ============ S I G N A L S ===========
        #   <ELEMENT> <EVENT>   <ACTION>     <SLOT> (func to call)
        self.spinBox.textChanged.connect(self.get_spin_value)
        self.change_label_color_bttn.clicked.connect(self.update_label_color)
        self.pushButton.clicked.connect(self.clear_spin_box)
        self.checkBox.clicked.connect(self.check_box_chnged)
        self.checkBox_2.clicked.connect(self.check_box_chnged)
        self.checkBox_3.clicked.connect(self.check_box_chnged)
        self.tool_box_pg2_bttn_1.clicked.connect(self.show_pop_up)
        # ======================================

        # Show the GUI.
        self.show()

    def update_label_color(self):
        # Get the current style of self.warning_label
        # Toggle between pre-defined pass and fail colors.
        if self.warning_label.styleSheet() == self.fail_color:
            style = self.pass_color
        else:
            style = self.fail_color
        # Set self.warning_label label to the new color
        self.warning_label.setStyleSheet(style)
        #  Set the text in  self.style_sheet_box to the new color.
        self.style_sheet_box.setText(style)

    def get_spin_value(self):
        # Get the spin box current value.
        spin_value = self.spinBox.text()
        # Set self.input_box to the spin box value.
        self.input_box.setText(spin_value)

    def clear_spin_box(self):
        # Clear input box
        self.input_box.clear()
        # Reset spin box value.
        self.spinBox.setValue(0)

    def check_box_chnged(self):
        # When multiple elements call the same function we can find
        # the caller using sender.
        sender = self.sender()
        print(sender.text(), 'was detected using sender.')

        # This is an example of getting an element type from a frame
        # and determining the sender.
        for cb in self.chec_box_frame.findChildren(Qt.QCheckBox):
            if cb.isChecked():
                print(cb.text(), 'was detected using findChildren')

    def show_pop_up(self):
        # Example of a custom pop up GUI.
        self.user_message.show_pop_message('ok', "User Message was selected with warning", 'warn')