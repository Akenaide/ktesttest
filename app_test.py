import sys
import unittest
from a2 import ope
from a3 import epo

from PyQt4 import QtGui, QtCore
from Ui_app_test import Ui_app_test

class app_test(QtGui.QWidget):

    def __init__(self):
        super(app_test, self).__init__()
        
        self.ui = Ui_app_test()
        self.ui.setupUi(self)
    
    def getX(self):
        return self.ui.lEX.value()
        
    def getY(self):
        return self.ui.lEY.value()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = app_test()
    myapp.show()
    print 'hello'
    sys.exit(app.exec_())