import sys
import unittest
from a2 import ope
from a3 import epo

from PyQt4 import QtGui, QtCore
from Ui_app_test import Ui_app

class app_test(QtGui.QMainWindow):

    def __init__(self):
        super(app_test, self).__init__()
        
        self.ui = Ui_app()
        self.ui.setupUi(self)
        self.ope = ope()
    
    def getX(self):
        return self.ui.lEX.text()
        
    def getY(self):
        return self.ui.lEY.text()
        
    def addi(self):
        self.ui.label_3.setText(str(self.ope.addi(self.getX(), self.getY())))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = app_test()
    myapp.show()
    print 'hello'
    sys.exit(app.exec_())
    
    