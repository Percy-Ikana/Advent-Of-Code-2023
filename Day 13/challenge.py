import time
import argparse
import sys
import copy
from os.path import join

#this only works becaue there is never a time more than one set of pairs 
#is more than one apart

def diffCount(lineOne, lineTwo, tolerance):
    return len([x for x in range(len(lineOne)) \
                if lineOne[x] != lineTwo[x]]) <= tolerance

def findReflectionPt2(grid, tolerance):
    #find points that might be reflections
    #aka, lines that match the next line
    reflections = []
    for line in range(len(grid)-1):
        if line == 2:
            pass
        reflection = (line, line+1)
        length = min(len(grid[:reflection[0]+1]),len(grid[reflection[0]+1:]))
        diff = \
            [diffCount(grid[reflection[0]-x], grid[reflection[1]+x], tolerance)\
            for x in range(length)]
        if all(diff):
            reflections.append(reflection)
    return set(reflections)

def rotateGrid(grid):
    return [''.join([row[col] for row in grid]) for col in range(len(grid[0]))]

def partOne(data):
    maps = [[x for x in set.split('\n')] for set in data.split('\n\n')]
    sumTotal = 0
    for map in maps:
        #Find y reflections
        yref = findReflectionPt2(map,0)
        mapFlip = rotateGrid(map)
        xref = findReflectionPt2(mapFlip,0)
        if yref is not None:
            sumTotal+=sum([len(map[:entry[0]+1])*100 for entry in yref])
        if xref is not None:
            sumTotal+=sum([len(mapFlip[:entry[0]+1]) for entry in xref])
    return sumTotal

def partTwo(data):
    maps = [[x for x in set.split('\n')] for set in data.split('\n\n')]
    sumTotal = 0
    for map in maps:
        #Find y reflections
        yref = findReflectionPt2(map,1) - findReflectionPt2(map,0)
        mapFlip = rotateGrid(map)
        xref = findReflectionPt2(mapFlip,1) - findReflectionPt2(mapFlip,0)
        if yref is not None:
            sumTotal+=sum([len(map[:entry[0]+1])*100 for entry in yref])
        if xref is not None:
            sumTotal+=sum([len(mapFlip[:entry[0]+1]) for entry in xref])
    return sumTotal

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
    fileName =join(sys.path[0],( "input" if args.test else "TestInput"))
    main(fileName)