import time
import argparse
import sys
import copy
from os.path import join
import math
from math import gcd

def partOne(data):
    path, maps = data.split('\n\n')
    maps = {line[:3]:{'L':line[7:10], 'R':line[12:15]} for line in maps.split('\n')}
    curLoc = 'AAA'
    curindex = 0
    while True:
        curLoc = maps[curLoc][path[curindex%len(path)]]
        curindex += 1
        if curLoc == 'ZZZ': return curindex

def partTwo(data):
    path, maps = data.split('\n\n')
    maps = {line[:3]:{'L':line[7:10], 'R':line[12:15]} for line in maps.split('\n')}
    maps['111'] = {'L':'111','R':'111'} #this is a break state, it goes nowhere.
    curLoc = [x for x in maps.keys() if x[2] == 'A']
    Origin = copy.deepcopy(curLoc)
    curindex = 0
    outIndex = {}
    while True:
        curLoc = [maps[way][path[curindex%len(path)]] for way in curLoc]
        curindex += 1
        for loc in range(len(curLoc)):
            if curLoc[loc][2] == 'Z':
                outIndex[Origin[loc]] = curindex
                curLoc[loc] = '111'
        if len(set(curLoc)) == 1:
            break
    
    lcm = 1
    for i in [outIndex[x] for x in outIndex.keys()]:
        lcm = lcm*i//gcd(lcm, i)
    return lcm
        

def main(fileName):
    data = []
    with open(fileName, 'r') as file:
        data = file.read()

    start_time = time.time()
    
    print(partOne(data))
    print(partTwo(data))
    
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--test', help='use the test input or not', 
                        action='store_false', required=False)
    args = parser.parse_args()
    fileName =join(sys.path[0],( "input" if args.test else "Testinput"))
    main(fileName)