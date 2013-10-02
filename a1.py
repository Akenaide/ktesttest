import nose
from a2 import ope

ope = ope()

def test_add():
	assert ope.addi(1,1) == 2
	
def test_add3():	
	assert ope.addi(1,1,1) == 3

def  test_div():
	assert ope.div(4,2) == 2
	assert ope.div(6,2) == 3
	
def test_divinverrt():	
	assert ope.div(3,6) == 2

def test_souss():
	assert ope.souss(4,2) == 2
	
def test_soussinvert():
	assert ope.souss(2,4) == -2
	
def test_mixdivandadd():
	assert ope.div(ope.addi(10,6),ope.addi(2,6)) == 2