import sys
import unittest
import ope
import epo

from Pyqt4.QtCore import Qt
from Ui_app_test import Ui_app_test

class app_test(QtGui.QWidget):

    def __init__(self):
        super(app_test, self).__init__()
        
        self.ui = Ui_app_test()
        self.ui.setupUi(self)
        