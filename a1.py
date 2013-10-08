import nose
from a2 import ope
from a3 import epo

a2 = ope()
a3 = epo()
def setUp(self) :
    print "Yay"

def tearDown(self):
    print "Sob sob"
 
def test_add():
	assert a2.addi(1,1) == 2
	
def test_add3():	
	assert a2.addi(1,1,1) == 3

def  test_div():
	assert a2.div(4,2) == 2
	assert a2.div(6,2) == 3
	
def test_divinverrt():	
	assert a2.div(3,6) == 2

def test_souss():
	assert a2.souss(4,2) == 2
	
def test_soussinvert():
	assert a2.souss(2,4) == -2
	
def test_mixdivandadd():
	assert a2.div(a2.addi(10,6),a2.addi(2,6)) == 2
	
def test_much():
	assert a2.noce() == 0
	
def test_conc():
	assert a3.conc("a","a") == "aa"
    
def test_nop():
    assert a3.nop() == "nop"