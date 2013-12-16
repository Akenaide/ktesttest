from nose.core import  TextTestRunner 
from nose.case import Test
from nose.loader import TestLoader 
import os.path as path
import sys
TOP_DIR = path.realpath(path.dirname(__file__))

def main():
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--nose", action="store_true",
            help="run nose")
    parser.add_argument("-u", "--unittest", action="store_true",
            help="run unittest",
            )

    args = parser.parse_args()
    
    if args.nose is not False :
         run_nose()

def run_nose():
    tl = TestLoader()
    ts = tl.loadTestsFromDir(tl.workingDir)
    rlst = TextTestRunner(stream=sys.stderr, descriptions=1, verbosity=2)
    tests = []
    for test in ts : 
        tests += test

    for test in tests :
        if type(test) == Test :
            test.runTest(rlst)
    #import pdb;pdb.set_trace()
    return rlst 

if __name__ == '__main__':
    main()
