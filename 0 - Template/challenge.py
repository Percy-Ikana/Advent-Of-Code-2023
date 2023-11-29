import time
import argparse
import sys
import copy
from os.path import join

def partOne(data):
    pass

def partTwo(data):
    pass

def main(fileName):
    data = ''
    with open(fileName, 'r') as file:
        data = file.readlines()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--test', help='use the test input or not', action='store_false', required=False)
    args = parser.parse_args()
    fileName =join(sys.path[0],( "input" if args.test else "Testinput"))
    
    print(fileName)

    startTime = start_time = time.time()

    main(fileName)
    
    print("--- %s seconds ---" % (time.time() - start_time))

