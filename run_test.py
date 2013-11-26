
from nose.loader import TestLoader 
import os.path as path

TOP_DIR = path.realpath(path.dirname(__file__))
def main():
    import argparse
    import sys
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--nose", action="store_true",
            help="run nose")
    parser.add_argument("-u", "--unittest", action="store_true",
            help="run unittest",
            )

    args = parser.parse_args()
    
    if args.unittest is not False :

        if args.nose is not False :
             
            run_nose() 
        else :
            print args.unittest

def run_nose():
    print "hey"
    testloader = TestLoader()
    for test in testloader.loadTestsFromDir(TOP_DIR):
        test.runTest()
        dir(test)

if __name__ == '__main__':
    main()
