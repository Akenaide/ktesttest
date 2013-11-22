import nose 

def main():
    import argparse
    import sys

    
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--nose", action="store_true",
            help="run nose")
    parser.add_argument("-u", "--unittest", action="store_true",
            help="run unittest",
            const="-v")

    args = parser.parse_args()
    
    if args.unittest is not False :

        if args.nose is not False :
             
            #args=None
            backup, sys.argv = sys.argv, sys.argv[:1] + ["-v"]
            nose.run()
            sys.argv = backup
    
        else :
            print args.unittest

if __name__ == '__main__':
    main()
