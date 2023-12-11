import time
import argparse
import sys
import copy
from os.path import join

def expandGalaxy(map, mul):
    filledX = set([x for x,_ in map])
    filledy = set([y for _,y in map])
    xrange = range(min(filledX),max(filledX)+1)
    yrange = range(min(filledy),max(filledy)+1)
    #we now have all points, what rows are empty, 
    # and the range the points take up
    
    Xpandmap = {}
    expand = 0
    for x in xrange:
        if x not in filledX:
            #we have a point that needs expanding
            expand+=1*mul
        Xpandmap[x] = expand

    Ypandmap = {}
    expand = 0
    for y in yrange:
        if y not in filledy:
            #we have a point that needs expanding
            expand+=1*mul
        Ypandmap[y] = expand
    for index in range(len(map)):
        point = map[index]
        map[index] = (point[0]+Xpandmap[point[0]],point[1]+Ypandmap[point[1]])
    #the map is expanded.
    pass
    
def calulateDistances(map):
    disances = {}
    for point in map:
        for otherPoint in map:
            if point is not otherPoint:
                pointKey = frozenset([point, otherPoint])
                disances[pointKey] = abs(otherPoint[0] - \
                                         point[0])+abs(otherPoint[1] - point[1])
    return disances

def partOne(data):
    map = [(x,y) for y in range(len(data)) for x in range(len(data[y])) \
           if data[y][x] == '#']
    expandGalaxy(map, 1)
    return sum([x[1] for x in calulateDistances(map).items()])

def partTwo(data):
    map = [(x,y) for y in range(len(data)) for x in range(len(data[y])) \
           if data[y][x] == '#']
    #this needs to be one lower to be right and I have no idea why, lol wtf
    #Ill look into this later. Probably not.
    expandGalaxy(map, 999999)
    return sum([x[1] for x in calulateDistances(map).items()])

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