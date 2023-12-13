import time
import argparse
import sys
import copy
from os.path import join

def partOne(data):
    rows = [([group for group in row.replace('.',' ').split()], [int(num) for num in broken.split(',')]) for line in data for row, broken in [line.split()]]
    #we now have to go through all the groups, we only care abut ones with ?, since toherwise trivial.
    pass

def partTwo(data):
    pass

def main(fileName):
    data = []
    with open(fileName, 'r') as file:
        data = file.readlines()

    start_time = time.time()
    
    print(partOne(data))
    print(partTwo(data))
    
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--test', help='use the test input or not', 
                        action='store_false', required=False)
    args = parser.parse_args()
    fileName =join(sys.path[0],( "input" if args.test else "TestInput"))
    main(fileName)