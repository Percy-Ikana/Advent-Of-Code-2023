#This is a fucking disaster

import time
import argparse
import sys
import copy
from os.path import join
import random


pipes = {'|':set(['N','S']),
           '-':set(['E','W']),
           'L':set(['N','E']),
           'J':set(['N','W']),
           '7':set(['W','S']),
           'F':set(['E','S']),}

pipeToArt = {'|':'│',
           '-':'─',
           'L':'└',
           'J':'┘',
           '7':'┐',
           'F':'┌'}

flip = {'W':'E','E':'W','N':'S','S':'N'}

moves = {'N':(0,-1),'S':(0,1),'E':(1,0),'W':(-1,0),}

def repalceStart(map, startPos):
    surround = {}
    connect = set()
    for x in range(-1,2):
        for y in range(-1,2):
            add = False
            if abs(x+y) == 1:
                if (startPos[0]+x,startPos[1]+y) in map.keys():
                    #we need to see what pipes can actually connect here, 
                    # so if we are at -x, we need to only allow E connections
                    #+x west, -y north, +y south
                    stepPoss = pipes[map[(startPos[0]+x,startPos[1]+y)]]
                    if x == -1 and 'E' in stepPoss:
                        add = True
                        connect.add('W')
                    if x == 1 and 'W' in stepPoss:
                        add = True
                        connect.add('E')
                    if y == -1 and 'S' in stepPoss:
                        add = True
                        connect.add('N')
                    if y == 1 and 'N' in stepPoss:
                        add = True
                        connect.add('S')
                    if add:
                        surround[(x,y)] = map[(startPos[0]+x,startPos[1]+y)]
    #Now we have a list of only valid connections, so can determine what the 
    #start value (I shold have just hard coded this, why am I not, fuck.)
    map[startPos] = list(pipes.keys())[list(pipes.values()).index(connect)]

def findValidStep(map, pos, backtrack):
    surround = {}
    connect = set()
    posPipe = map[pos]
    validMoves = ({'N', 'E', 'S', 'W'} - set(flip[backtrack]))\
        .intersection(pipes[posPipe])
    #We have the only valid, non backtrack move, so we take it, 
    # and return the new position, and the direction
    #For LATER: I dunno, actually check the move is valid, lol
    
    return (list(validMoves)[0], moves[list(validMoves)[0]])

def buildLoop(map, start):
    dirCame = flip[random.choice(list(pipes[map[start]]))]
    pos = start
    pipeTrail = [(start, dirCame)]
    while True:
        #take a step, we know the direction we came from, 
        #so we dont go back that way
        dir, move = findValidStep(map,pos,dirCame)
        dirCame = dir
        pos = (pos[0]+move[0],pos[1]+move[1])
        pipeTrail.append((pos, dirCame))
        if pos == start:
            break
    return pipeTrail

#this stupidly checks every non-pipe trail point on the map, becasue this is
#faster than my attempt to find only points that are contained, then
#check them.
def checkpoints(map):
    count = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            #dont check the trail itself
            point = map[y][x]
            if point == '.':
                left = ''.join(map[y][:x]).replace('-','').replace('F','')\
                    .replace('7','').replace('S','').replace('.','')
                if len(left)%2 == 1:
                    count+=1
    return count

#My original solution was to print this out, and literally 
#find the empty points using the paintbucket in Kirta. it worked.
def printMap(trailmap, map):
    cordList = [cord for cord,dir in trailmap[:-1]]
    text = []
    for y in range(140):
        for x in range(140):
            text.append(pipeToArt[map[(x,y)]] if (x,y) in cordList else '.')
        text.append('\n')
    print(''.join(text))

def removeExtras(map, trailMap):
    mapN = copy.deepcopy(map)
    trailPoints = [cord for cord,dir in trailMap[:-1]]
    for y in range(len(mapN)):
        for x in range(len(mapN[y])):
            mapN[y][x] = '.' if (x,y) not in trailPoints else mapN[y][x]
    return mapN

def partOne(data):
    map = {(y,x):data[x][y] for x in range(len(data)) for y \
           in range(len(data[x].strip())) if data[x][y] is not '.'}
    start = list(map.keys())[list(map.values()).index('S')]
    repalceStart(map, start)
    trail = buildLoop(map, start)
    
    return (len(trail)-1)//2

def partTwo(data):
    map = {(y,x):data[x][y] for x in range(len(data)) for y \
           in range(len(data[x].strip())) if data[x][y] is not '.'}
    fullMap = [[elem for elem in x.strip()] for x in data]
    start = list(map.keys())[list(map.values()).index('S')]
    repalceStart(map, start)
    trail = buildLoop(map, start)
    printMap(trail, map)
    newMap = removeExtras(fullMap, trail)

    return checkpoints(newMap)

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