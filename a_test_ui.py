import nose
import sys
import unittest
from app_test import app_test
from PyQt4.QtGui import QApplication
from PyQt4.QtTest import QTest
from PyQt4.QtCore import Qt

class App_test_test(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.app_test = app_test()
        
    def test_addition(self):
        QTest.keyClicks(self.app_test.ui.lEX, "3")
        QTest.keyClicks(self.app_test.ui.lEY, "3")
        QTest.mouseClick(self.app_test.ui.pButtonAdd, Qt.LeftButton)
        self.assertEqual(self.app_test.ui.label_3.text() ,"6")
    
    def test_soustraction(self):
        QTest.keyClicks(self.app_test.ui.lEX, "3")
        QTest.keyClicks(self.app_test.ui.lEY, "3")
        QTest.mouseClick(self.app_test.ui.pButtonSou, Qt.LeftButton)
        self.assertEqual(self.app_test.ui.label_3.text() ,"0")
    
    def test_multi(self):
        QTest.keyClicks(self.app_test.ui.lEX, "3")
        QTest.keyClicks(self.app_test.ui.lEY, "5")
        QTest.mouseClick(self.app_test.ui.pButtonMul, Qt.LeftButton)
        self.assertEqual(self.app_test.ui.label_3.text() ,"15")