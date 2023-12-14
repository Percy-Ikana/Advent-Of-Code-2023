import time
import argparse
import sys
import copy
from os.path import join
from functools import lru_cache
from frozendict import frozendict

#this allows python to remember the result of functions with matching args, it a huge speedup, since it just skips those branches.
@lru_cache(maxsize=100, typed=False)
def getBound(start, dir, bound):
    if dir == 0:
        #we arent moving in this direction, so we just return its own val
        return range(start,start+1)
    if dir < 0:
        #we are moving into the negative
        return range(start, bound[0]-1,-1)
    if dir > 0:
        #we are moving into the negative
        return range(start, bound[1],1)
    return 0

def printGrid(grid,bounds):
    string = ''
    for y in range(bounds[1][1]):
        for x in range(bounds[0][1]):
            string = string + (grid[(x,y)] if (x,y) in grid else ' ')
        string = string + '\n'
    print(string)

def calcOffset(grid, dir, bounds):
    originX, originY = 0 ,0
    if dir[0] == 1:
        originX = bounds[0][0]
    if dir[0] == 0:
        originX = 0
    if dir[0] == -1:
        originX = bounds[0][1]
    
    if dir[1] == 1:
        originY = bounds[1][0]
    if dir[1] == 0:
        originY = 0
    if dir[1] == -1:
        originY = bounds[1][1]
    #we have the origins to count from
    load = 0
    for rock in grid:
        if grid[rock] == 'O':
            #calc the offset from the origin point
            load += abs((rock[0]-originX)*dir[0]) + abs((rock[1]-originY)*dir[1])
    return load


#direction is a tuple, in the form (tiltX, tiltY), where -1 is north, or west,
#and 1 is south or east. 
#for bounds, thats the edges of the map, where we move things to
#this allows python to remember the result of functions with matching args, it a huge speedup, since it just skips those branches.
@lru_cache(maxsize=10000, typed=False)
def tilt(rockDict, bounds,  direction):
    #Now we have to actually tilt the grid.
    #we start at the corner, or side, that is closest to the tilt edge, so we
    #can move those rocks first, I think that sould work to keep this non 
    #recursive. We just move them as far as possible, and that sould be the end.
    #the complexity here is still going to be high, o^2 or more
    #sort thr rock by the keys, we use direction to determine how to sort said keys.
    sortedRocks = dict(sorted(rockDict.items(), key=lambda item:(item[0][0]*direction[0],item[0][1]*direction[1]), reverse=True))
    # so now we have the rocks in order, so we check to see the farthest spot they can move to in the dir specified.
    #typecast to a set so we can modify it as we go, since we should only be modding the current element, should be fine
    for rock in list(sortedRocks):
        #if its not a rock that can move, we skip it.
        if rockDict[rock] == 'O':
            #get the bounds we care about
            xRange = getBound(rock[0], direction[0], bounds[0])
            yRange = getBound(rock[1], direction[1], bounds[1])
            #we now have the bounds as ranges
            inBounds = all([rock[0] in xRange, rock[1] in yRange])
            #current offset
            curOff = (0,0)
            while inBounds:
                #move in the dir specified
                newOff = (curOff[0]+direction[0],curOff[1]+direction[1])
                newPos = (rock[0]+newOff[0],rock[1]+newOff[1])
                #if its in out dict we are done, cant move.
                if not all([newPos[0] in xRange, newPos[1] in yRange]) or newPos in sortedRocks.keys():
                    break
                curOff = newOff
            if curOff != (0,0):
                del sortedRocks[rock]
                sortedRocks[(rock[0]+curOff[0],rock[1]+curOff[1])] = rockDict[rock]
    return sortedRocks


def partOne(data):
    #grid = [[x if x != '.' else ' ' for x in row.strip()] for row in data]
    dictGrid = {(x,y):data[y][x] for y in range(len(data)) for x in range(len(data[y])) if data[y][x] != '.' and data[y][x] != '\n'}
    bounds = ((0,len(data[0].strip())),(0,len(data)))
    tilted = tilt(frozendict(dictGrid), bounds,  (0,-1))
    #printGrid(tilted, bounds)
    return calcOffset(tilted, (0,-1), bounds)

def partTwo(data):
    dictGrid = {(x,y):data[y][x] for y in range(len(data)) for x in range(len(data[y])) if data[y][x] != '.' and data[y][x] != '\n'}
    bounds = ((0,len(data[0].strip())),(0,len(data)))
    tilted = copy.deepcopy(dictGrid)
    seenGrids = []
    loopLen = 0
    firstSeen = 0
    for i in range(1000000000):
        for each in [(0,-1),(-1,0),(0,1),(1,0)]:
            tilted = tilt(frozendict(tilted), bounds,  each)
        #printGrid(tilted, bounds)
        if frozendict(tilted) in seenGrids:
            #we have this this before, everything else is a loop
            firstSeen = seenGrids.index(frozendict(tilted))
            loopLen = i - seenGrids.index(frozendict(tilted))
            #so we have to calculate how
            break
        else:
            seenGrids.append(frozendict(tilted))

    ran = range((1000000000 - firstSeen)%loopLen-1)
    for i in ran:
        for each in [(0,-1),(-1,0),(0,1),(1,0)]:
            tilted = tilt(frozendict(tilted), bounds,  each)
    #printGrid(tilted, bounds)
    #96003
    return calcOffset(tilted, (0,-1), bounds)

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