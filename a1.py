import nose
from a2 import ope
from a3 import epo

epo = epo()
ope = ope()
def setUp(self) :
    print "Yay"

def tearDown(self):
    print "Sob sob"
 
def test_add(self):
	assert ope.addi(1,1) == 2
	
def test_add3(self):	
	assert ope.addi(1,1,1) == 3

def  test_div(self):
	assert ope.div(4,2) == 2
	assert ope.div(6,2) == 3
	
def test_divinverrt(self):	
	assert ope.div(3,6) == 2

def test_souss(self):
	assert ope.souss(4,2) == 2
	
def test_soussinvert(self):
	assert ope.souss(2,4) == -2
	
def test_mixdivandadd(self):
	assert ope.div(ope.addi(10,6),ope.addi(2,6)) == 2
	
def test_much(self):
	assert ope.noce() == 0
	
def test_conc(self):
	assert epo.conc("a","a") == "aa"